#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Tweet(models.Model):
    """Tweet class"""

    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # not needed since tweets have no titles
    # def __str__(self):
    #     """String method"""
        
    #     return self.title
    
    def get_absolute_url(self):
        return reverse("tweet_detail", kwargs={"pk": self.pk})
    