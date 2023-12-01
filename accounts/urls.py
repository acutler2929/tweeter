#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import path
from .views import SignUpView, ProfileViewPublic, ProfileViewPrivate

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "public_profile/<int:pk>/", ProfileViewPublic.as_view(), name="profile_public"
    ),
    # path("profile/<int:pk>", ProfileViewPrivate.as_view(), name="profile_private"),
]
