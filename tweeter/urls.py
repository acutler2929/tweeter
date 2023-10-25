#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import path
from .views import IndexPageView

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
]
