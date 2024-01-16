from django.contrib import admin

from membership.models import Membership, MembershipSeason

# Register your models here.
admin.site.register(Membership)
admin.site.register(MembershipSeason)
