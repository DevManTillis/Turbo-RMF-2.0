from django.http import JsonResponse
import json
from winrm.protocol import Protocol

# Command Processing
def remote_command(ip_addr, admin_username, admin_password, command):
    powershell = 'powershell -c'
    results = list()

    p = Protocol(
        endpoint='https://%s:5986/wsman' %(ip_addr),
        transport='ntlm',
        username=r'%s\%s'%(ip_addr, admin_username),
        password='%s' %(admin_password),
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, powershell,[command])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)
    results.append(std_out)
    results.append(std_err)
    results.append(status_code)
    if (results[2] == 0):
        return results[0].decode('utf-8')
    else:
        return results[1].decode('utf-8')

def RunCommand(request):
    json_data = json.loads(request.body)
    u_initiate = remote_command(
        json_data.get("ip_addr"),
        json_data.get('admin_username'),
        json_data.get('admin_password'),
        json_data.get('command')
        )
    return JsonResponse(u_initiate, safe=False)



from upload.models import *

# Form view
def index(request):
    crap = "Hello World!"
    return render(request, 'theform/index.html', {'crap': crap})

def vulns(request,pk):
    #crap = pk
    return render(request, 'theform/index_vulns.html', {'pk': pk})

# Checklists Uploader
from django.core.files.storage import FileSystemStorage
from upload.models import Checklist, Vuln
from .forms import DocumentForm
from django.utils import timezone

# Checklist Parser
from shutil import copyfile
from xml.dom.minidom import parse
import xml.dom.minidom
from pathlib import Path

def process_xml(data):
    # Create main list
    master_vuln_list = []

    # Open XML document using minidom parser

    #DOMTree = xml.dom.minidom.parse(data)
    DOMTree = xml.dom.minidom.parseString(data)
    collection = DOMTree.documentElement

    VULNS = collection.getElementsByTagName("VULN")
    vuln_count = len(VULNS)

    i = 0
    while i < vuln_count:
        # create list
        #vuln_list = []
        vuln_dict = {}


        # DEFINE CHECKLIST DATA ELEMENTS
        vulnid = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[0]
        severity = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[1]
        vulndiscuss = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[6]
        checkcontent = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[8]
        fixtext = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[9]
        stigref = VULNS[i].getElementsByTagName("ATTRIBUTE_DATA")[21]
        status = VULNS[i].getElementsByTagName("STATUS")[0]
        finding_details = VULNS[i].getElementsByTagName("FINDING_DETAILS")[0]
        comments = VULNS[i].getElementsByTagName("COMMENTS")[0]
        # IF XML ELEMENT CONTAINS DATA THEN PRINT THE DATA IF NOT PRINT "NO DATA"
        def check_for_value(value):
            if value.childNodes.length == 0:
                return str("NO DATA")
            else:
                return str(value.childNodes[0].data)

        v_id = check_for_value(vulnid)
        v_sev = check_for_value(severity)
        v_dis = check_for_value(vulndiscuss)
        v_con = check_for_value(checkcontent)
        v_fix = check_for_value(fixtext)
        v_ref = check_for_value(stigref)
        v_sta = check_for_value(status)
        Comments = check_for_value(comments)
        v_det = check_for_value(finding_details)

        vuln_dict = {
            "vulnid":v_id,"severity":v_sev,"vulndiscuss":v_dis,
            "checkcontent":v_con,"fixtext":v_fix,"stigref":v_ref,
            "status":v_sta,"comments":Comments,"finding_details":v_det,
            }

        # add list to main list
        master_vuln_list.append(vuln_dict)

        i += 1
    return master_vuln_list


# Checklist upload
def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        context = "Authenticated!"
        return render(request, 'upload/index.html', {'context': context})
    else:
        # Do something for anonymous users.
        context = "Sorry NOT Authed!"
        return render(request, 'upload/index.html', {'context': context})


# FILE UPLOAD
def run(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        myfile.seek(0)
        data = b''
        chunks = myfile.chunks(chunk_size=None)
        for chunk in chunks:
            data += chunk
        # change byte file to UTF-8
        doc_data = str(data.decode(encoding='utf-8'))
        doc_name = str(myfile.name)
        doc_owner = str(request.user)
        c = Checklist(checklist_text=doc_name,checklist_owner=doc_owner, pub_date=timezone.now())
        c.save()
        # get private key

        sqlrow = Checklist.objects.get(pk=c.id)

        checklist_doc = process_xml(doc_data)
        for vuln in checklist_doc:
            sqlrow.vuln_set.create(
            v_ids = str(vuln["vulnid"]),vuln_text = str(vuln["vulnid"]),
            v_sev = str(vuln["severity"]),
            v_dis = str(vuln["vulndiscuss"]),
            v_con = str(vuln["checkcontent"]),
            v_fix = str(vuln["fixtext"]),
            v_ref = str(vuln["stigref"]),
            v_sta = str(vuln["status"]),
            Comments = str(vuln["comments"]),
            v_det = str(vuln["finding_details"])
                )
        
            
        return render(request, 'upload/simple_upload.html', {
            'doc_data': doc_data,
            'doc_name': doc_name,
            'doc_owner': doc_owner
        })
    return render(request, 'upload/simple_upload.html')

def xml(request):
    return render(request, 'upload/test.html')
