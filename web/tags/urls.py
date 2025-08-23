from django.urls import path
from .views import *

app_name = "tags"

urlpatterns = [path("", TagsListMobileView.as_view(), name="list")]
