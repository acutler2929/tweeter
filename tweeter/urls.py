#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
