#       Alice Cutler
#       CIS 218
#       October 25, 2023
from typing import Any
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
# from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy, reverse

from .forms import ReplyForm
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


class TweetDetailView(LoginRequiredMixin, SingleObjectMixin, FormView):
    """Tweet Detail View"""

    model = Tweet
    form_class = ReplyForm
    template_name = "tweet_detail.html"

    def get(self, request, *args, **kwargs):
        # Call the get_object method and store it in the instance of
        # the View so that it can be used later in the form_valid method.
        self.object = self.get_object()
        # Do whatever the parent would have done
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Save the form, which will behind the scenes make an
        # instance of the comment model. The commit=False prevents
        # it from actually saving.
        reply = form.save(commit=False)
        # Set the FK of tweet on the reply to class's object.
        # Which is an instance of Tweet since this view uses
        # the Tweet model.
        reply.tweet = self.object
        # Add the user to it.
        reply.author = self.request.user
        # Save the reply for real this time.
        reply.save()
        # Do whatever the parent would do
        return super().form_valid(form)

    def get_success_url(self):
        tweet = self.get_object()
        return reverse("tweet_detail", kwargs={"pk": tweet.pk})


class TweetCreateView(LoginRequiredMixin, CreateView):
    """Tweet Create View"""

    model = Tweet
    template_name = "new_tweet.html"
    fields = ("body",)
    success_url = reverse_lazy("tweet_feed")

    def form_valid(self, form):
        """Set author to whoever is logged in"""
        form.instance.author = self.request.user
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
    

class TweetLikeView(LoginRequiredMixin, View):
    """Tweet Like View"""

    def get(self, request, *args, **kwargs):
        """GET request"""

        # Fetch data that was sent by ajax from the request object.
        tweet_id = request.GET.get("tweet_id", None)
        tweet_action = request.GET.get("tweet_action", None)
        # If there is no data, return an Error JSON Response
        if not tweet_id or not tweet_action:
            return JsonResponse(
                {
                    "success": False,
                }
            )
        
        # Got data, Gonna use it to update the likes
        tweet = Tweet.objects.get(id=tweet_id)
        if tweet_action == "like":
            tweet.likes.add(request.user)
        else:
            tweet.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )


class ProfileViewPublic(LoginRequiredMixin, ListView):
    """Public Profile View"""
    # TODO:


class ProfileViewPrivate(LoginRequiredMixin, UserPassesTestMixin):
    """Private Profile View"""
    # TODO:
