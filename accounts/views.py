#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    """Sign Up View"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileViewPublic(LoginRequiredMixin, DetailView):
    """Public Profile View"""

    # TODO: customize to specific user

    model = CustomUser
    template_name = "profile_public.html"

    def get_queryset(self):
        query = super().get_queryset()
        # query.order_by("-date")

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProfileViewPrivate(LoginRequiredMixin, UserPassesTestMixin):
    """Private Profile View"""

    # TODO:
