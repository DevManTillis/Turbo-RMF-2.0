from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("projects", views.ProjectViewSet)
router.register("check-list", views.CheckListViewSet)

router.register("stig", views.StigViewSet)
router.register("check-list-item", views.CheckListItemViewSet)

router.register("vuln-fix", views.VulnFixViewSet)
router.register("vuln-remove", views.VulnRemoveViewSet)

router.register("test-suite", views.TestSuiteViewSet)
router.register("device", views.DeviceViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
