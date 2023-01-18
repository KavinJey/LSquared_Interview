from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .content.views import DevicesListView, ImageListView, ContentEventCreateView

router = DefaultRouter()
router.register(r"devices", DevicesListView)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/images/", ImageListView.as_view()),
    path("api/v1/content/", ContentEventCreateView.as_view()),
    
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
