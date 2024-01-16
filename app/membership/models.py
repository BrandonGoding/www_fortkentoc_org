from decimal import Decimal

from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


User._meta.get_field("email")._unique = True


class MembershipTypeChoices(models.TextChoices):
    ADULT = "AD", "Adult"
    YOUTH = "YH", "Youth"
    FAMILY = "FM", "Family"
    UMFK = "UM", "UMFK Student"

    @staticmethod
    def get_membership_price(membership_type):
        if membership_type == MembershipTypeChoices.ADULT:
            return Decimal(75)
        if (
            membership_type == MembershipTypeChoices.YOUTH
            or membership_type == MembershipTypeChoices.UMFK
        ):
            return Decimal(40)
        if membership_type == MembershipTypeChoices.FAMILY:
            return Decimal(185)
        raise ValueError(f"Unknown membership type {membership_type}")


class MembershipSeason(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"

    def year(self):
        return self.end_date.year

    def save(self, *args, **kwargs):
        if self.current:
            MembershipSeason.objects.filter(current=True).exclude(
                pk=self.pk
            ).update(current=False)
        super().save(*args, **kwargs)


class Membership(models.Model):
    session_key = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    type = models.CharField(
        max_length=2, choices=MembershipTypeChoices.choices
    )
    season = models.ForeignKey("MembershipSeason", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=0, max_digits=3)

    def __str__(self):
        return f"{self.member} - {self.type} - {self.season}"


class Member(models.Model):
    membership = models.ForeignKey("Membership", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()  # NEED TO BE UNIQUE OR NULL
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
