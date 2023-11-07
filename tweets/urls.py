#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.urls import path

from .views import (
    TweetFeedView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,
)

urlpatterns = [
    path("", TweetFeedView.as_view(), name="tweet_feed"),
    path("new/", TweetCreateView.as_view(), name="tweet_new"),
    path("<int:pk>/edit", TweetUpdateView.as_view(), name="tweet_edit"),
    path("<int:pk>/delete", TweetDeleteView.as_view(), name="tweet_delete"),
]
