from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Document(models.Model):
    document_version = models.CharField(max_length=200, default='NONE')
    document_name = models.CharField(max_length=200, default='NONE')
    document_owner = models.CharField(max_length=200, default='NONE')
    document_data = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document_name
    def __str__(self):
        return self.document_owner
    def __str__(self):
        return self.document_data

class Checklist(models.Model):
    checklist_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    checklist_name = models.CharField(max_length=200)
    checklist_owner = models.CharField(max_length=200)
    def __str__(self):
        return self.checklist_text

class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ['checklist_text', 'pub_date', 'checklist_name','checklist_owner']


class Vuln(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    v_ids = models.CharField(max_length=200,default='NONE')
    vuln_text = models.CharField(max_length=200,default='NONE')

    #v_sev = models.CharField(max_length=200,default='NONE')
    v_sev = models.CharField(max_length=200,default='NONE')
    v_dis = models.CharField(max_length=15000,default='NONE')
    v_con = models.CharField(max_length=15000,default='NONE')
    v_fix = models.CharField(max_length=15000,default='NONE')
    Finding_Details = models.CharField(max_length=200,default='NONE')
    v_ref = models.CharField(max_length=200,default='NONE')
    v_sta = models.CharField(max_length=200,default='NONE')
    Comments = models.CharField(max_length=200,default='NONE')
    v_det = models.CharField(max_length=200,default='NONE')
    v_command = models.CharField(max_length=9000,default='NONE')
    v_remove_fix = models.CharField(max_length=9000,default='NONE')
    v_command_status = models.CharField(max_length=9000,default='NONE')
    v_command_enabled = models.CharField(max_length=9000,default='NONE')
    
#        v_det = models.CharField(max_length=200, default='NONE')

class VulnForm(ModelForm):
    class Meta:
        model = Vuln
        fields = ['v_ids', 'v_sev','v_dis','v_con','v_fix','Finding_Details','v_ref','v_sta','Comments','v_det']
from django.db import models
from django.forms import ModelForm
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Command(models.Model):
    v_command = models.CharField(max_length=200)
    def __str__(self):
        return self.command
