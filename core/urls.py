from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from core.views import *
from core.views.user import UserViewSet

router = DefaultRouter()
router.register(r"pets", PetView)
router.register(r"users", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("token/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
]
