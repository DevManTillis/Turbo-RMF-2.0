from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from . import serializers
from . import models 

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id", "name"]


class CheckListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckListSerializer
    queryset = models.CheckList.objects.all()

    filter_backends = [filters.SearchFilter]
    #search_fields = ["project_id__project_id"]


class StigViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StigSerializer
    queryset = models.Stig.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]


class CheckListItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CheckListItemSerializer
    queryset = models.CheckListItem.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]


class VulnFixViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VulnFixSerializer
    queryset = models.VulnFix.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]


class VulnRemoveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VulnRemoveSerializer
    queryset = models.VulnRemove.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]


class TestSuiteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TestSuiteSerializer
    queryset = models.TestSuite.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeviceSerializer
    queryset = models.Device.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ["project_id__project_id"]
