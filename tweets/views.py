#       Alice Cutler
#       CIS 218
#       October 25, 2023
from typing import Any
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy

from .models import Tweet


class TweetFeedView(LoginRequiredMixin, ListView):
    """Tweet Feed View"""

    model = Tweet
    template_name = "tweet_feed.html"

    def get_queryset(self):
        query = super().get_queryset()
        query.order_by("-date")

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["stuff"] = "My new template stuff"
        return context


class TweetDetailView(DetailView):
    """Tweet Detail View"""

    model = Tweet
    template_name = "tweet_detail.html"


class TweetCreateView(LoginRequiredMixin, CreateView):
    """Tweet Create View"""

    model = Tweet
    template_name = "new_tweet.html"
    fields = (
        "body",
        "author",
    )
    success_url = reverse_lazy("tweet_feed")

    def form_valid(self, form):
        """Set author to whoever is logged in"""
        form.instance.author = self.request.author
        return super().form_valid(form)


class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Tweet Update View"""

    model = Tweet
    fields = ("body",)
    template_name = "edit_tweet.html"
    # success_url = reverse_lazy("tweet_feed")

    def test_func(self):
        """Test method that is required by UserPassesTestMixin
        Allows for arbitrary checking of criteria to know if
        user can visit view"""
        obj = self.get_object()

        return obj.author == self.request.user


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Tweet View"""

    model = Tweet
    template_name = "delete_tweet.html"
    success_url = reverse_lazy("tweet_feed")

    def test_func(self):
        """Test method that is required by UserPassesTestMixin
        Allows for arbitrary checking of criteria to know if
        user can visit view"""
        obj = self.get_object()

        return obj.author == self.request.user


# TODO:
# class CommentAddView(CreateView):
#     """Comment Add View"""

#     model = ???
#     fields = ???
#     template_name = ???
#     success_url = ???


# TODO: add profile views? or do they go in accounts???
