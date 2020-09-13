from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ("project_id", "project_name", )
        depth = 1


class CheckListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CheckList
        #fields = ("project_id", "checklist_id", "json_config", "stig")
        fields = "__all__"


class StigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Stig
        fields = ("project_id", "stig_id")


class CheckListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CheckListItem
        fields = ("project_id", "checklist_item_id", "checklist_id", "vuln_id", 
                  "fix_id", "removal_id", "vuln_text", "vuln_sev", "vuln_discussion",
                  "vuln_check_content", "vuln_finding_details", "vuln_reference", 
                  "vuln_status", "vuln_comments")


class VulnFixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VulnFix
        fields = ("project_id", "fix_id", "fix_url", "removal_id", "checklist_item_id",
                  "fix_status", "last_run_time")


class VulnRemoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VulnRemove
        fields = ("project_id", "remove_id", "fix_id", "fix_url", "removal_id",
                  "checklist_item_id", "remove_status", "last_run_time")


class TestSuiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TestSuite
        fields = ("project_id", "suite_id", "checklist_id", 
                  "suite_url", "last_run_time", "suite_status")


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Device
        fields = ("project_id", "device_id", "last_run_time", "suite_test")
