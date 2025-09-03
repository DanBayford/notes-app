from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .forms import UserThemeForm, UserFontForm
from .models import ProfileModel


class SettingsMenuView(LoginRequiredMixin, TemplateView):
    template_name = "settings/settings.html"


class SettingsThemeView(LoginRequiredMixin, FormView):
    template_name = "settings/theme.html"
    form_class = UserThemeForm

    """
    Pass the appropriate ProfileModel instrance to populate form
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = get_object_or_404(ProfileModel, user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("settings:theme")


class SettingsFontView(LoginRequiredMixin, FormView):
    template_name = "settings/font.html"
    form_class = UserFontForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = get_object_or_404(ProfileModel, user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("settings:font")


class SettingsPasswordView(LoginRequiredMixin, TemplateView):
    template_name = "settings/password.html"
