from django.contrib import admin
from membership.models import ActivitiesEnjoyed, Membership, MembershipSeason

# Register your models here.
admin.site.register(Membership)
admin.site.register(MembershipSeason)
admin.site.register(ActivitiesEnjoyed)
