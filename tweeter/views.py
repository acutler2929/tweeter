#       Alice Cutler
#       CIS 218
#       October 25, 2023

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home Page View"""

    template_name = "home.html"
