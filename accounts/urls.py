#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
