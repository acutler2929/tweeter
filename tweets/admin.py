#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.contrib import admin
from .models import Tweet, Reply


class ReplyInline(admin.StackedInline):
    """Reply Inline"""

    model = Reply


class TweetAdmin(admin.ModelAdmin):
    """Tweet Admin"""

    inlines = [ReplyInline]


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Reply)
