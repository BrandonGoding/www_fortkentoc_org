import json
from datetime import datetime

import pytz
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import stripe
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from membership.models import (
    Membership,
    MembershipSeason,
    MembershipTypeChoices,
    Member,
)
from membership.forms import (
    MembershipFormStep1,
    MembershipFormStep2,
    MembershipFormStep3,
)


def membership_form_step_1(request):
    if request.session.session_key is None:
        request.session.create()

    if request.method == "POST":
        form = MembershipFormStep1(request.POST)
        if form.is_valid():
            try:
                membership = Membership.objects.get(
                    session_key=request.session.session_key
                )
                membership.type = form.cleaned_data["type"]
                membership.price = MembershipTypeChoices.get_membership_price(
                    form.cleaned_data["type"]
                )
                membership.save()
            except Membership.DoesNotExist:
                Membership.objects.create(
                    type=form.cleaned_data["type"],
                    season=MembershipSeason.objects.get(current=True),
                    price=MembershipTypeChoices.get_membership_price(
                        form.cleaned_data["type"]
                    ),
                    session_key=request.session.session_key,
                )
            return redirect(reverse("memberships:onboarding_member_partial"))
    form = MembershipFormStep1()
    try:
        membership = Membership.objects.get(
            session_key=request.session.session_key
        )
    except ObjectDoesNotExist:
        membership = None
    return render(
        request,
        "website/partials/memberships/membership_type_form.html",
        {
            "form": form,
            "membership_type": membership.type if membership else None,
        },
    )


def membership_form_step_2(request):
    members = None
    membership = Membership.objects.get(
        session_key=request.session.session_key
    )
    if request.method == "POST":
        form = MembershipFormStep2(request.POST)
        if form.is_valid():
            membership.member_set.all().delete()
            new_member = form.save(commit=False)
            new_member.membership_id = membership.id
            new_member.save()
            address = form.cleaned_data["address"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zip_code = form.cleaned_data["zip_code"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
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
                    address=address,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    phone=phone,
                    email=email,
                    membership_id=membership.id,
                )

            return redirect(
                reverse("memberships:onboarding_activities_enjoyed_partial")
            )
    else:
        members = membership.member_set.all()
        form = MembershipFormStep2(
            instance=membership.member_set.first()
            if membership.member_set.exists()
            else None
        )
    return render(
        request,
        "website/partials/memberships/membership_member_form.html",
        {
            "form": form,
            "membership": membership,
            "members": members[1:] if members else None,
        },
    )


def membership_form_step_3(request):
    membership = Membership.objects.get(
        session_key=request.session.session_key
    )
    if request.method == "POST":
        form = MembershipFormStep3(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("memberships:onboarding_confirmation_partial")
            )
    else:
        form = MembershipFormStep3(instance=membership)
    return render(
        request,
        "website/partials/memberships/membership_activities_form.html",
        {"form": form},
    )


def membership_form_step_4(request):
    membership = Membership.objects.get(
        session_key=request.session.session_key
    )
    members = membership.member_set.all()
    membership_price = MembershipTypeChoices.get_membership_price(
        membership.type
    )
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price": f"{MembershipTypeChoices.get_membership_strip_api_price_id(membership.type)}",
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url="http://localhost:8000"
                + reverse("memberships:welcome_new_member"),
                cancel_url="http://localhost:8000"
                + reverse("memberships:canceled"),
                automatic_tax={"enabled": True},
                client_reference_id=request.session.session_key,
            )
        except Exception as e:
            return str(e)
        return redirect(checkout_session.url)
    return render(
        request,
        "website/partials/memberships/membership_confirmation_checkout.html",
        {
            "membership": membership,
            "members": members,
            "membership_price": membership_price,
        },
    )


@csrf_exempt
def membership_stripe_callback_url(request):
    if request.method == "GET":
        return HttpResponse(status=405)
    try:
        event = stripe.Event.construct_from(
            json.loads(request.body), settings.STRIPE_SECRET_KEY
        )
    except ValueError as e:
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "checkout.session.completed":
        payment_intent = event.data.object
        try:
            membership = Membership.objects.get(
                session_key=payment_intent["client_reference_id"]
            )
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        tz = pytz.timezone("America/New_York")
        membership.square_timestamp = datetime.fromtimestamp(
            payment_intent["created"], tz
        )
        membership.session_key = None
        membership.save()
        request.session.flush()
        return HttpResponse(status=200)
    return HttpResponse(status=400)


class MembershipFormNameField(TemplateView):
    template_name = (
        "website/partials/memberships/membership_member_form_name_fields.html"
    )
