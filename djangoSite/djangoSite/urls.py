from django.conf import settings
from django.contrib import admin

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

import notifications.urls

urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path(r"^notifications/", include(notifications.urls, namespace='notifications')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
