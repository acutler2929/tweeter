#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    """Sign Up View"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileViewPublic(LoginRequiredMixin, DetailView):
    """Public Profile View"""

    model = CustomUser
    template_name = "profile_public.html"

    def get_queryset(self):
        query = super().get_queryset()
        # query.order_by("-date")

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileViewPrivate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Private Profile View"""

    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("tweet_feed")
    template_name = "profile_private.html"

    def get_queryset(self):
        query = super().get_queryset()

        return query

    def test_func(self):
        """Test method that is required by UserPassesTestMixin
        Allows for arbitrary checking of criteria to know if
        user can visit view"""
        obj = self.get_object()

        return obj.username == self.request.user.username
