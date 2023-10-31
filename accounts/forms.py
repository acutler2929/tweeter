#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custon User Creation Form"""

    class Meta:
        model = CustomUser
        # EXPLICIT fields definition
        fields = (
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta:
        model = CustomUser
        # IMPLICIT fields definition
        fields = UserChangeForm.Meta.fields
