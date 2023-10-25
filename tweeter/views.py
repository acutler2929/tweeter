#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    """Index Page View"""

    template_name = "index.html"
