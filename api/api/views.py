from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework import permissions
from . import serializers
from . import models 

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id", "name"]

    permission_classes = [permissions.IsAuthenticated]


class CheckListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckListSerializer
    queryset = models.CheckList.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class StigViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StigSerializer
    queryset = models.Stig.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class CheckListItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckListItemSerializer
    queryset = models.CheckListItem.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class VulnFixViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VulnFixSerializer
    queryset = models.VulnFix.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class VulnRemoveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VulnRemoveSerializer
    queryset = models.VulnRemove.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class TestSuiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TestSuiteSerializer
    queryset = models.TestSuite.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeviceSerializer
    queryset = models.Device.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]

    permission_classes = [permissions.IsAuthenticated]