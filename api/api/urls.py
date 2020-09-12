from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views 

router = DefaultRouter()
router.register("project", views.ProjectViewset)

router.register("command", views.CommandViewset)
router.register("playbook", views.PlaybookViewset)

router.register("ansible-configuration", views.AnsibleConfViewset)
router.register("host", views.HostViewset)

router.register("role", views.RoleViewset)
router.register("output", views.OutputViewset)

urlpatterns = [
    path("", include(router.urls)),
    path('schema/project/', views.ui_schema, name='ui_schema'),
]
