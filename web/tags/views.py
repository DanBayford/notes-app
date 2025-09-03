from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TagsListMobileView(LoginRequiredMixin, TemplateView):
    template_name = "tags/tagsListMobile.html"
