from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=70)

    def __str__(self):
        return self.project_name


class Command(models.Model):
    project_id = models.ForeignKey(Project, related_name='proj_id', on_delete=models.CASCADE)
    arguments = models.CharField(max_length=190)

    def __str__(self):
        return self.project_id.project_name


class Playbook(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    json_playbook = models.CharField(max_length=255)

    def __str__(self):
        return self.project_id.project_name


class AnsibleConfiguration(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    json_config = models.CharField(max_length=120)

    def __str__(self):
        return self.project_id.project_name


class Host(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.project_id.project_name


class Role(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    role_url = models.URLField()

    def __str__(self):
        return self.project_id.project_name


class Output(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    json_output = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.project_id.project_name
