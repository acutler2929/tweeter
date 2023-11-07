#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy

from .models import Tweet


class TweetFeedView(ListView):
    """Tweet Feed View"""

    model = Tweet
    template_name = "tweet_feed.html"


class TweetCreateView(CreateView):
    """Tweet Create View"""

    model = Tweet
    template_name = "new_tweet.html"
    fields = (
        "body",
        "date",
        "author",
    )
    success_url = reverse_lazy("tweet_feed")


class TweetUpdateView(UpdateView):
    """Tweet Update View"""

    model = Tweet
    fields = (
        "body",
        "date",
    )
    template_name = "edit_tweet.html"


class TweetDeleteView(DeleteView):
    """Delete Tweet View"""

    model = Tweet
    template_name = "delete_tweet.html"


# TODO:
# class CommentAddView(CreateView):
#     """Comment Add View"""

#     model = ???
#     fields = ???
#     template_name = ???
#     success_url = ???


# TODO: add profile views? or do they go in accounts???
