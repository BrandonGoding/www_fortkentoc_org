import json
from datetime import datetime

import pytz
import stripe
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from membership.forms import (MembershipFormStep1, MembershipFormStep2,
                              MembershipFormStep3)
from membership.models import (Member, Membership, MembershipSeason,
                               MembershipTypeChoices)

# Constants


def get_membership_by_session_key(session_key):
    try:
        return Membership.objects.get(session_key=session_key)
    except Membership.DoesNotExist:
        return None


class MembershipFormStep1View(View):
    template_name = "website/partials/memberships/membership_type_form.html"

    def get_session_key(self, request):
        session_key = request.session.session_key
        if not session_key:
            request.session.create()

    def get(self, request):
        self.get_session_key(request)
        membership = get_membership_by_session_key(request.session.session_key)
        form = MembershipFormStep1(instance=membership)

        context = {
            "form": form,
            "membership_type": membership.type if membership else None,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        self.get_session_key(request)
        membership = get_membership_by_session_key(request.session.session_key)
        form = MembershipFormStep1(request.POST, instance=membership)

        if form.is_valid():
            membership = form.save(commit=False)
            membership.season = MembershipSeason.objects.get(current=True)
            membership.session_key = request.session.session_key
            membership.price = MembershipTypeChoices.get_membership_price(
                form.cleaned_data["type"]
            )
            membership.save()

            return redirect(reverse("memberships:onboarding_member_partial"))

        context = {
            "form": form,
            "membership_type": membership.type if membership else None,
        }

        return render(request, self.template_name, context)


class MembershipFormStep2View(View):
    template_name = "website/partials/memberships/membership_member_form.html"

    def get(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        members = membership.member_set.all() if membership else None
        form = MembershipFormStep2(
            instance=members.first() if members else None
        )

        context = {
            "form": form,
            "membership": membership,
            "members": members[1:] if members else None,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        members = membership.member_set.all() if membership else None
        form = MembershipFormStep2(
            request.POST, instance=members.first() if members else None
        )

        if form.is_valid():
            # Delete existing members associated with this membership
            if members:
                members.delete()

            # Create new member
            new_member = form.save(commit=False)
            new_member.membership = membership
            new_member.save()

            # Create additional members
            additional_first_names = request.POST.getlist(
                "first_name_additional"
            )
            additional_last_names = request.POST.getlist(
                "last_name_additional"
            )

            for first_name, last_name in zip(
                additional_first_names, additional_last_names
            ):
                Member.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    address=form.cleaned_data["address"],
                    city=form.cleaned_data["city"],
                    state=form.cleaned_data["state"],
                    zip_code=form.cleaned_data["zip_code"],
                    phone=form.cleaned_data["phone"],
                    email=form.cleaned_data["email"],
                    membership=membership,
                )

            return redirect(
                reverse("memberships:onboarding_activities_enjoyed_partial")
            )

        context = {
            "form": form,
            "membership": membership,
            "members": members[1:] if members else None,
        }

        return render(request, self.template_name, context)


class MembershipFormStep3View(View):
    template_name = (
        "website/partials/memberships/membership_activities_form.html"
    )

    def get(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        form = MembershipFormStep3(instance=membership)

        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        form = MembershipFormStep3(request.POST, instance=membership)

        if form.is_valid():
            form.save()
            return redirect(
                reverse("memberships:onboarding_confirmation_partial")
            )

        context = {"form": form}

        return render(request, self.template_name, context)


class MembershipFormStep4View(View):
    template_name = (
        "website/partials/memberships/membership_confirmation_checkout.html"
    )

    def get(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        members = membership.member_set.all() if membership else None
        membership_price = (
            MembershipTypeChoices.get_membership_price(membership.type)
            if membership
            else None
        )

        context = {
            "membership": membership,
            "members": members,
            "membership_price": membership_price,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        membership = get_membership_by_session_key(request.session.session_key)
        if not membership:
            return redirect(reverse("memberships:canceled"))

        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price": MembershipTypeChoices.get_membership_strip_api_price_id(
                            membership.type
                        ),
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=f"{settings.BASE_URL}{reverse('memberships:welcome_new_member')}",
                cancel_url=f"{settings.BASE_URL}{reverse('memberships:canceled')}",
                automatic_tax={"enabled": True},
                client_reference_id=request.session.session_key,
            )
        except stripe.error.StripeError as e:
            return str(e)

        return redirect(checkout_session.url)


@method_decorator(csrf_exempt, name="dispatch")
class MembershipStripeCallbackView(View):
    def handle_checkout_completed_event(self, event_data):
        try:
            membership = Membership.objects.get(
                session_key=event_data["client_reference_id"]
            )
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        self.send_email(membership.email)
        tz = pytz.timezone("America/New_York")
        membership.square_timestamp = datetime.fromtimestamp(
            event_data["created"], tz
        )
        membership.session_key = None
        membership.save()
        self.request.session.flush()
        return HttpResponse(status=200)

    def send_email(self, email):
        send_mail(
            "Welcome to your membership",
            "Thank you for joining The Fort Kent Outdoor Center.  Before we can finish processing your "
            "membership we need a release form filled out for each member.  Once we receive your release form we will"
            " send your parking decals and welcome letter. Please complete the release form at this link: "
            "https://waiver.smartwaiver.com/w/61670215255e2/web/",
            "info@fortkentoc.org",
            ["info@fortkentoc.org", email],
            fail_silently=True,
        )

    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            event_data = json.loads(request.body)
            event = stripe.Event.construct_from(event_data, stripe.api_key)
        except ValueError as e:
            return HttpResponse(status=400)

        if event.type == "checkout.session.completed":
            return self.handle_checkout_completed_event(event.data.object)

        return HttpResponse(status=400)


class MembershipFormNameField(TemplateView):
    template_name = (
        "website/partials/memberships/membership_member_form_name_fields.html"
    )
