from django import forms

from membership.models import Membership


class MembershipFormStep1(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['type']


class MembershipFormStep2(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['type']


class MembershipFormStep3(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['type']
