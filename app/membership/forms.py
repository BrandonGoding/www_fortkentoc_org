from django import forms

from membership.models import Membership, Member


class MembershipFormStep1(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["type"]


class MembershipFormStep2(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "email", "phone", "address", "city", "state", "zip_code"]


class MembershipFormStep3(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["type"]
