from django.urls import path
from .views import *

app_name = "settings"

urlpatterns = [
    path("", SettingsMenuView.as_view(), name="menu"),
    path("theme/", SettingsThemeView.as_view(), name="theme"),
    path("font/", SettingsFontView.as_view(), name="font"),
    path("password-change/", SettingsPasswordView.as_view(), name="password-change"),
]
