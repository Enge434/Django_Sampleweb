from django.shortcuts import render
from django import forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .form import RenewPatientsForm,Sortform,Searchform
from django.views import generic
from django.http.response import JsonResponse
from .models import Patients, Clinic_information
from django.contrib.auth.decorators import permission_required
@permission_required('catalog.can_mark_returned')
# Create your views here.


def index(request):
    num_patients=Patients.objects.all().count()
    return render(
        request,
        'index.html',
        context = {'num_patients':num_patients},
    )

class PatientView(generic.ListView):

    model = Patients

class PatientDetailView(generic.DetailView):
    model = Patients

def display_all(request):
    model = Patients
    patients_list = Patients.objects.all()
    newlist=[]
    for patient_temp in patients_list:
        data={
            'id':patient_temp.id,
            'name': patient_temp.name,
            'specimen_type':patient_temp.specimen_type,
            'other_type':patient_temp.other_type,
            'collectiondate':patient_temp.collectiondate,
            'collectiontime':patient_temp.collectiontime,
            'hkid':patient_temp.hkid,
            'ethnicity':patient_temp.ethnicity,
            'sex': patient_temp.sex,
            'dob':patient_temp.dob,
            'referral':patient_temp.referral,
            'clinicid':patient_temp.clinicid,
            'doctor':patient_temp.doctor,
            'phone':patient_temp.phone,
            'fax':patient_temp.fax,
        }
        newlist.append(data)
    
        
    return render(request,'catalog/displaytable.html',{'patients_list':newlist})

def sortingori(request):
    form=Sortform(request.POST or None)
    patients_list = Patients.objects.all()

    if request.method=='POST':
        if form.is_valid():
            sortkey=form.cleaned_data['sortkey']
            print(patients_list)
            return HttpResponseRedirect(reverse('sorting',kwargs={'sortkey':sortkey}))
        else:
            return HttpResponseRedirect(reverse('sortingori'))
    return render(request,'catalog/sortingori.html',{'patients_list':patients_list,'form':form})

def searchori(request):
    formsearch=Searchform(request.POST or None)
    patients_list = Patients.objects.all()

    if request.method=='POST':
        
        if formsearch.is_valid():
            searchkey=formsearch.cleaned_data['searchkey']
            searchvalue=formsearch.cleaned_data['searchvalue']
            return HttpResponseRedirect(reverse('search',kwargs={'searchkey':searchkey,'searchvalue':searchvalue}))
        else:
            return HttpResponseRedirect(reverse('display'))
    return render(request,'catalog/searchori.html',{'patients_list':patients_list,'formsearch':formsearch})

def sorting(request,sortkey):
    model = Patients
    patients_list = Patients.objects.order_by(sortkey)
    form=Sortform(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            sortkey=form.cleaned_data['sortkey']
            print(patients_list)
            return HttpResponseRedirect(reverse('sorting',kwargs={'sortkey':sortkey}))
        else:
            return HttpResponseRedirect(reverse('sorting',kwargs={'sortkey':sortkey}))
 
    return render(request,'catalog/sorting.html',{'patients_list':patients_list,'form':form})

def renew_patients(request,pk):
    patient_temp = get_object_or_404(Patients,pk=pk)
    
    if request.method == 'POST':
        form = RenewPatientsForm(
            request.POST
        )
        if form.is_valid():
            patient_temp.specimen_type = form.cleaned_data['renew_specimen_type']
            patient_temp.other_type = form.cleaned_data['renew_other_type']
            
            patient_temp.collectiondate = form.cleaned_data['renew_collectiondate']
            patient_temp.collectiontime = form.cleaned_data['renew_collectiontime']
            patient_temp.name = request.POST.get('renew_name')
            patient_temp.hkid = form.cleaned_data['renew_hkid']
            patient_temp.ethnicity = form.cleaned_data['renew_ethnicity']
            patient_temp.sex = form.cleaned_data['renew_sex']
            patient_temp.dob = form.cleaned_data['renew_dob']
            patient_temp.clinicid = form.cleaned_data['renew_clinicid']
            patient_temp.doctor = form.cleaned_data['renew_doctor']
            patient_temp.phone = form.cleaned_data['renew_phone']
            patient_temp.fax = form.cleaned_data['renew_fax']
            patient_temp.referral = form.cleaned_data['renew_referral']
            patient_temp.clinic.diagnosis = form.cleaned_data['renew_diagnosis']
            patient_temp.clinic.previous = form.cleaned_data['renew_previous']
            patient_temp.clinic.spid = form.cleaned_data['renew_spid']
            patient_temp.clinic.celltype = form.cleaned_data['renew_celltype']
            patient_temp.clinic.other = form.cleaned_data['renew_other']
            form.fields['renew_stage'].initial = patient_temp.clinic.stage
            patient_temp.clinic.stage = form.cleaned_data['renew_stage']
            patient_temp.clinic.status = form.cleaned_data['renew_status']
            patient_temp.clinic.additional = form.cleaned_data['renew_additional']
            patient_temp.clinic.request = form.cleaned_data['renew_request']
            patient_temp.clinic.save()

            patient_temp.save()
            return HttpResponseRedirect(reverse('patients-detail',args=[str(patient_temp.id)]))
    else:
        form = RenewPatientsForm(initial={
            'renew_specimen_type': patient_temp.specimen_type,
            'renew_other_type': patient_temp.other_type,
            'renew_collectiondate':patient_temp.collectiondate,
            'renew_collectiontime':patient_temp.collectiontime,
            'renew_name': patient_temp.name,
            'renew_hkid':patient_temp.hkid,
            'renew_ethnicity':patient_temp.ethnicity,
            'renew_sex':patient_temp.sex,
            'renew_referral':patient_temp.referral,
            'renew_dob':patient_temp.dob,
            'renew_clinicid':patient_temp.clinicid,
            'renew_doctor':patient_temp.doctor,
            'renew_phone':patient_temp.phone,
            'renew_fax':patient_temp.fax,
            'renew_diagnosis':patient_temp.clinic.diagnosis,
            'renew_previous':patient_temp.clinic.previous,
            'renew_spid':patient_temp.clinic.spid,
            'renew_celltype':patient_temp.clinic.celltype,
            'renew_other':patient_temp.clinic.other,
            'renew_stage':patient_temp.clinic.stage,
            'renew_status':patient_temp.clinic.status,
            'renew_additional':patient_temp.clinic.additional,
            'renew_request':patient_temp.clinic.request,
        })
    return render(request, 'catalog/renew_patients.html',{'form':form,'patienttemp':patient_temp})

def add_patients(request):
    patient_temp = Patients()
    
    if request.method == 'POST':
        form = RenewPatientsForm(request.POST)
        if form.is_valid():
            clinic_temp=Clinic_information(
                clinic_name = form.cleaned_data['renew_name'],
                previous = form.cleaned_data['renew_previous'],
                spid = form.cleaned_data['renew_spid'],
                diagnosis = form.cleaned_data['renew_diagnosis'],
                celltype = form.cleaned_data['renew_celltype'],
                stage = form.cleaned_data['renew_stage'],
                status = form.cleaned_data['renew_status'],
                additional = form.cleaned_data['renew_additional'],
                request = form.cleaned_data['renew_request'],
                other = form.cleaned_data['renew_other']
                
            )
            clinic_temp.save()
            patient_temp=Patients(
                specimen_type = form.cleaned_data['renew_specimen_type'],
                other_type = form.cleaned_data['renew_other_type'],
                collectiondate = form.cleaned_data['renew_collectiondate'],
                collectiontime = form.cleaned_data['renew_collectiontime'],
                name = form.cleaned_data['renew_name'],
                hkid = form.cleaned_data['renew_hkid'],
                ethnicity = form.cleaned_data['renew_ethnicity'],
                sex = form.cleaned_data['renew_sex'],
                dob = form.cleaned_data['renew_dob'],
                referral = form.cleaned_data['renew_referral'],
                clinicid = form.cleaned_data['renew_clinicid'],
                doctor = form.cleaned_data['renew_doctor'],
                phone = form.cleaned_data['renew_phone'],
                fax = form.cleaned_data['renew_fax'],
                clinic = clinic_temp,
            )
            patient_temp.save()
            return HttpResponseRedirect(reverse('patients-detail',args=[str(patient_temp.id)]))
    else:
        form = RenewPatientsForm(initial={
            'renew_name': '',
            'renew_hkid':'',
            'renew_ethnicity':'',
            'renew_sex':'',
            'renew_dob':'',
            'renew_clinicid':'',
            'renew_doctor':'',
            'renew_phone':'',
            'renew_fax':'',
        })
    
    return render(request, 'catalog/add_patients.html',{'form':form,'patienttemp':patient_temp})

def delete_patients(request,pk):
    patient_temp = get_object_or_404(Patients,pk=pk)
    patient_temp.delete()
    
    return render(request, 'catalog/delete_patients.html')
import json
def jsondata(request,pk):
    patient_temp = get_object_or_404(Patients,pk=pk)
    data={
        'id':patient_temp.id,
        'name': patient_temp.name,
        'specimen_type':patient_temp.specimen_type,
        'other_type':patient_temp.other_type,
        'collectiondate':patient_temp.collectiondate,
        'collectiontime':patient_temp.collectiontime,
        'hkid':patient_temp.hkid,
        'ethnicity':patient_temp.ethnicity,
        'sex': patient_temp.sex,
        'dob':patient_temp.dob,
        'referral':patient_temp.referral,
        'clinicid':patient_temp.clinicid,
        'doctor':patient_temp.doctor,
        'phone':patient_temp.phone,
        'fax':patient_temp.fax,
    }
    

    return render(request,'catalog/datatable.html',{'data':json.dumps(data)})

def search(request,searchkey,searchvalue):
    model = Patients
    patients_list = Patients.objects.filter(**{searchkey:searchvalue})
    formsearch=Searchform(request.POST or None)
    if request.method=='POST':
        formsearch=Searchform(request.POST)
        if formsearch.is_valid():
            searchkey=formsearch.cleaned_data['searchkey']
            searchvalue=formsearch.cleaned_data['searchvalue']
            return HttpResponseRedirect(reverse('search',kwargs={'searchkey':searchkey,'searchvalue':searchvalue}))
        else:
            form=Sortform(initial={
                'searchkey':searchkey,
                'searchvalue':searchvalue,
            })
            return HttpResponseRedirect(reverse('display'))
    return render(request,'catalog/search.html',{'formsearch':formsearch,'patients_list':patients_list})