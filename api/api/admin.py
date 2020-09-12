from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Command)
admin.site.register(models.Playbook)
admin.site.register(models.AnsibleConfiguration)
admin.site.register(models.Host)
admin.site.register(models.Role)
admin.site.register(models.Output)