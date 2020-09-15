from rest_framework_simplejwt import views as auth_views
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("register", views.Register)

urlpatterns = [
    path("login/", auth_views.TokenObtainPairView.as_view()),
    path("my-profile/", views.MyAccount.as_view()),
    path("", include(router.urls))
]
