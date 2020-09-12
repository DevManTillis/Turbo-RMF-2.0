from rest_framework import viewsets
from rest_framework import filters
from . import serializers
from . import models 
from django.http import JsonResponse


def ui_schema(request):
    SCHEMA = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]
    return JsonResponse(SCHEMA, safe=False)


# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']


class CommandViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CommandSerializer
    queryset = models.Command.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']


class PlaybookViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PlaybookSerializer
    queryset = models.Playbook.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']


class AnsibleConfViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AnsibleConfigurationSerializer
    queryset = models.AnsibleConfiguration.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']


class HostViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HostSerializer
    queryset = models.Host.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']


class RoleViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']


class OutputViewset(viewsets.ModelViewSet):
    serializer_class = serializers.OutputSerializer
    queryset = models.Output.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_id__id']
