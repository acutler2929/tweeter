#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django import forms

from .models import Reply


class ReplyForm(forms.ModelForm):
    """Reply Form"""

    class Meta:
        model = Reply
        fields = ("reply",)