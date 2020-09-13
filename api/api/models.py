from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.project_name


class CheckList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    checklist_name = models.CharField(max_length=36, unique=True)
    checklist_id = models.AutoField(primary_key=True)
    json_config = models.TextField(max_length=1000)
    stig = models.CharField(max_length=36)

    def __str__(self):
        return self.checklist_name


class Stig(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    stig_id = models.CharField(max_length=36, unique=True, primary_key=True)

    def __str__(self):
        return self.stig_id

class CheckListItem(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    checklist_item_id = models.CharField(max_length=36, unique=True)
    checklist_id = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    vuln_id = models.CharField(max_length=36)
    fix_id = models.CharField(max_length=36, unique=True)
    removal_id = models.CharField(max_length=36, unique=True)
    vuln_text = models.TextField(max_length=1500)
    vuln_sev = models.CharField(max_length=36)
    vuln_discussion = models.TextField(max_length=1500)
    vuln_check_content = models.TextField(max_length=1500)
    vuln_finding_details = models.TextField(max_length=1500)
    vuln_reference = models.TextField(max_length=1500)
    vuln_status = models.CharField(max_length=36)
    vuln_comments = models.TextField(max_length=1500)

    def __str__(self):
        return self.checklist_item_id


class VulnFix(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    fix_id = models.CharField(max_length=36, unique=True, primary_key=True)
    fix_url = models.URLField(unique=True)
    removal_id = models.CharField(max_length=36)
    checklist_item_id = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    fix_status = models.CharField(max_length=36)
    last_run_time = models.CharField(max_length=36)

    def __str__(self):
        return self.fix_id


class VulnRemove(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    remove_id = models.CharField(max_length=36, unique=True, primary_key=True)
    fix_id = models.CharField(max_length=36, unique=True)
    fix_url = models.URLField(unique=True)
    removal_id = models.CharField(max_length=36)
    checklist_item_id = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    remove_status = models.CharField(max_length=36)
    last_run_time = models.CharField(max_length=36)

    def __str__(self):
        return self.removal_id


class TestSuite(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    suite_id = models.CharField(max_length=36, unique=True, primary_key=True)
    checklist_id = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    suite_url = models.URLField(unique=True)
    last_run_time = models.CharField(max_length=36)
    suite_status = models.CharField(max_length=36)

    def __str__(self):
        return self.suite_id


class Device(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=36, unique=True, primary_key=True)
    last_run_time = models.CharField(max_length=36)
    suite_test = models.CharField(max_length=36)

    def __str__(self):
        return self.device_id



