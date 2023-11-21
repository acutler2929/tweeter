#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from tweets.models import Tweet, Reply


class ApiReplyDetailView(LoginRequiredMixin, View):
    """Reply Detail View"""

    def get(self, request, tweet_pk, reply_pk, *args, **kwargs):
        """Handle GET request"""

        reply = Reply.objects.values().get(pk=reply_pk)
        return JsonResponse(reply, safe=False)


class ApiReplyListView(LoginRequiredMixin, View):
    """API Reply List View"""

    def get(self, request, tweet_pk, *args, **kwargs):
        """Handle GET request"""

        replies = list(Reply.objects.filter(tweet__id=tweet_pk).values())
        return JsonResponse(replies, safe=False)


class ApiTweetDetailView(LoginRequiredMixin, View):
    """Api Tweet Detail View"""

    def get(self, request, tweet_pk, *args, **kwargs):
        """Handle GET request"""

        tweet = Tweet.objects.values().get(pk=tweet_pk)
        replies = list(Reply.objects.filter(tweet__id=tweet_pk).values())
        tweet["replies"] = replies
        return JsonResponse(tweet, safe=False)


class ApiTweetFeedView(LoginRequiredMixin, View):
    """Api Tweet Feed View"""

    def get(self, request, *args, **kwargs):
        """Handle GET request"""

        tweets = list(Tweet.objects.values())
        return JsonResponse(tweets, safe=False)
