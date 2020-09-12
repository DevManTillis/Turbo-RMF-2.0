from rest_framework import serializers
from . import models 


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ("id", "project_name", )
        depth = 1


class CommandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Command
        fields = "__all__"

class PlaybookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Playbook
        fields = ("id", "project_id", "name", "json_playbook", )


class AnsibleConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AnsibleConfiguration
        fields = ("id", "project_id", "json_config", )


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Host
        fields = ("id", "project_id", "name", )


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ("id", "project_id", "name", "role_url", )


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Output
        fields = ("id", "project_id", "json_output", "start_time", 
                  "end_time", "status", )

