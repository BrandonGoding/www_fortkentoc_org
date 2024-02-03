from rest_framework import serializers

from membership.models import Membership, MembershipTypeChoices


class MembershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipTypeChoices


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
