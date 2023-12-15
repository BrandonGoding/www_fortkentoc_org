from django.db import models


# Create your models here.
class MembershipTypeChoices(models.TextChoices):
    ADULT = "AD", "Adult"
    YOUTH = "YH", "Youth"
    FAMILY = "FM", "Family"
    UMFK = "UM", "UMFK Student"


class MembershipSeason(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"


class Membership(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    membership_type = models.CharField(
        max_length=2, choices=MembershipTypeChoices.choices
    )
    membership_season = models.ForeignKey(
        "MembershipSeason", on_delete=models.CASCADE
    )
    parent_member = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.member} - {self.membership_type} - {self.membership_season}"


class Member(models.Model):
    user = models.OneToOneField(
        "auth.User", on_delete=models.SET_NULL, null=True, blank=True
    )
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
