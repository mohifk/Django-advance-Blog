from django.urls import path, include
from .. import views

urlpatterns = [
    # profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
