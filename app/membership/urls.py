from django.urls import path
from membership import views

app_name = "memberships"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]
