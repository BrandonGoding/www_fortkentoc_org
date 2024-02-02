from django import forms
from localflavor.us.forms import USStateSelect
from membership.models import ActivitiesEnjoyed, Member, Membership


class MembershipFormStep1(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["type"]


class MembershipFormStep2(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "width": "half",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "width": "half",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "width": "half",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "width": "half",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "width": "full",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "width": "third",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    state = forms.CharField(
        widget=USStateSelect(
            attrs={
                "width": "third",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    zip_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "width": "third",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )

    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "zip_code",
        ]


class MembershipFormStep3(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["activities_enjoyed"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the activities_enjoyed field to use checkboxes
        self.fields[
            "activities_enjoyed"
        ].widget = forms.CheckboxSelectMultiple()

        # You can also customize the queryset for the activities_enjoyed field
        self.fields[
            "activities_enjoyed"
        ].queryset = ActivitiesEnjoyed.objects.all()
