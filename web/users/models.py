from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import AppThemeEnum, AppFontEnum

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # type: ignore

    def __str__(self):
        return self.email


class ProfileModel(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    theme = models.CharField(
        max_length=10, choices=AppThemeEnum.choices(), default=AppThemeEnum.LIGHT.name
    )
    font = models.CharField(
        max_length=10, choices=AppFontEnum.choices(), default=AppFontEnum.SANS.name
    )

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self):
        return f"{self.user.email}'s profile"

    def get_user_theme(self):
        return self.theme

    def get_user_font(self):
        return self.font
