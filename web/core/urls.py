from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('health.urls'))
]

if settings.DEBUG:
    import debug_toolbar # type: ignore

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # path("__reload__/", include("django_browser_reload.urls")),
    ] + urlpatterns

else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)