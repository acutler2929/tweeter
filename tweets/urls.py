#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.urls import path

from .views import (
    TweetFeedView,
    TweetCreateView,
    TweetDetailView,
    TweetUpdateView,
    TweetDeleteView,
    TweetLikeView,
)

urlpatterns = [
    path("", TweetFeedView.as_view(), name="tweet_feed"),
    path("new/", TweetCreateView.as_view(), name="tweet_new"),
    path("<int:pk>/", TweetDetailView.as_view(), name="tweet_detail"),
    path("<int:pk>/edit", TweetUpdateView.as_view(), name="tweet_edit"),
    path("<int:pk>/delete", TweetDeleteView.as_view(), name="tweet_delete"),
    path("<int:pk>/like/", TweetLikeView.as_view(), name="tweet_like"),
]
