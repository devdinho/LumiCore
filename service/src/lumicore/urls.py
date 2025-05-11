from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from authentication.api import CreateProfileRestView, ProfileRestView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

router = DefaultRouter(trailing_slash=False)
router.register(
    "api/register/", CreateProfileRestView, basename="CreateProfileRestView"
)
router.register("api/profile", ProfileRestView, basename="ProfileRestView")

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)