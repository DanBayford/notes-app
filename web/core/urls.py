from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, SignupView, LogoutView  # type:ignore


urlpatterns = [
    path("notes/", include("notes.urls")),
    path("settings/", include("users.urls")),
    path("tags/", include("tags.urls")),
    path("admin/", admin.site.urls),
    path('login/', LoginView.as_view(success_url="/notes", template_name="allauth/login.html"), name="account_login"),
    path('signup/', SignupView.as_view(success_url="/notes" ,template_name="allauth/signup.html"), name="account_signup"),
    path('logout/', LogoutView.as_view(template_name="allauth/logout.html"), name="account_logout"), # logout URL set in base.py 
    path("", include("health.urls")),
]

if settings.DEBUG:
    import debug_toolbar  # type: ignore

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        path("__reload__/", include("django_browser_reload.urls")),
    ] + urlpatterns

else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
