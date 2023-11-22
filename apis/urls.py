#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.urls import path

from .views import (
    ApiReplyDetailView,
    ApiReplyListView,
    ApiTweetDetailView,
    ApiTweetFeedView,
)

urlpatterns = [
    path(
        "tweets/<int:tweet_pk>/replies/<int:reply_pk>/",
        ApiReplyDetailView.as_view(),
        name="api_reply_detail",
    ),
    path(
        "tweets/<int:tweet_pk>/tweet_feed/",
        ApiReplyListView.as_view(),
        name="api_reply_list",
    ),
    path(
        "tweets/<int:tweet_pk>/",
        ApiTweetDetailView.as_view(),
        name="api_tweet_detail",
    ),
    path(
        "tweets/",
        ApiTweetFeedView.as_view(),
        name="api_tweet_list",
    ),
]
