from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ProfileModel

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class UserThemeForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ("theme",)
        widgets = {"theme": forms.RadioSelect}


class UserFontForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ("font",)
        widgets = {"font": forms.RadioSelect}
