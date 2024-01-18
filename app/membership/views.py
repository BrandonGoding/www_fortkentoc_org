from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.views.generic import TemplateView

from membership.models import (
    Membership,
    MembershipSeason,
    MembershipTypeChoices, Member,
)
from membership.forms import (
    MembershipFormStep1,
    MembershipFormStep2,
    MembershipFormStep3,
)


# season = models.ForeignKey("MembershipSeason", on_delete=models.CASCADE)
# price = models.DecimalField(decimal_places=0, max_digits=3)


def membership_form_step_1(request):
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
    membership = Membership.objects.get(
        session_key=request.session.session_key
    )
    if request.method == "POST":
        form = MembershipFormStep2(request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.membership_id = membership.id
            new_member.save()
            address = form.cleaned_data["address"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zip_code = form.cleaned_data["zip_code"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            additional_first_names = request.POST.getlist('first_name_additional')
            additional_last_names = request.POST.getlist('last_name_additional')

            for first_name, last_name in zip(additional_first_names, additional_last_names):
                Member.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    phone=phone,
                    email=email,
                    membership_id=membership.id
                )

            return redirect(
                reverse("memberships:onboarding_activities_enjoyed_partial")
            )
    else:
        form = MembershipFormStep2()
    return render(
        request,
        "website/partials/memberships/membership_member_form.html",
        {"form": form, "membership": membership},
    )


def membership_form_step_3(request):
    if request.method == "POST":
        form = MembershipFormStep3(request.POST)
        if form.is_valid():
            return redirect(
                reverse("memberships:onboarding_confirmation_partial")
            )
    else:
        form = MembershipFormStep3()
    return render(
        request,
        "website/partials/memberships/membership_activities_form.html",
        {"form": form},
    )


def membership_form_step_4(request):
    if request.method == "POST":
        form = MembershipFormStep1(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = MembershipFormStep1()
    return render(
        request,
        "website/partials/memberships/membership_member_form.html",
        {"form": form},
    )


class MembershipFormNameField(TemplateView):
    template_name = "website/partials/memberships/membership_member_form_name_fields.html"
