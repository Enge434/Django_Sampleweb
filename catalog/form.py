from django import forms

class RenewPatientsForm(forms.Form):
    renew_name = forms.CharField(max_length=20,label='Name')
    renew_specimen_type = forms.CharField(
        max_length = 20,
        label='Specimen Type',
        widget=forms.widgets.RadioSelect(choices=[("Blood","Blood"),("Pleural Fluid","Pleural Fluid"),('Others','Others')])
    )
    renew_other_type = forms.CharField(max_length=30,label='Other type',required=False)
    renew_collectiondate = forms.CharField(max_length=20,label='Collection Date',help_text='YYYY-MM-DD')
    renew_collectiontime = forms.CharField(max_length=10, label='Collection Time', help_text='Style: HH:MM')
    
    renew_hkid = forms.CharField(max_length=20,label='HKID')
    renew_ethnicity = forms.CharField(max_length=20,label='Ethnicity',required = False)
    renew_sex = forms.CharField(
        max_length=20,
        label='Sex',
        widget=forms.widgets.RadioSelect(choices=[('F','F'),('M','M'),('Prefer not to say','Prefer not to say')]),
        required = True
    )
    renew_referral = forms.CharField(max_length=50, label = 'Referral Site')
    renew_dob = forms.CharField(max_length=20,label='Date of Birth',help_text='YYYY-MM-DD')
    renew_clinicid = forms.CharField(max_length=20,label='Clinic ID',required=False)
    renew_doctor = forms.CharField(max_length=20,label='Referral Doctor')
    renew_phone = forms.CharField(max_length=20,label='Phone Number',required=False)
    renew_fax = forms.CharField(max_length=20,label='Fax Number',required=False)
    renew_previous = forms.CharField(
        max_length=3,
        label='Has patient preformed p-EGFR test in Sanomics previously?',
        widget=forms.widgets.RadioSelect(choices=[('Yes','Yes'),('No','No')]),
        required=True
    )
    renew_spid = forms.CharField(max_length=10, label = 'Sanomics Patient ID',required = False)
    renew_diagnosis = forms.CharField(
        max_length=20,
        label='Diagnosis of Lung Cancer',
        widget=forms.widgets.RadioSelect(choices=[('Confirmed','Confirmed'),('Pending','Pending')]),
        required=True
    )
    renew_celltype = forms.CharField(
        max_length = 50,
        label='Histological Cell Type',
        widget=forms.widgets.RadioSelect(choices=[
            ('Adenocarcinoma','Adenocarcinoma'),
            ('Squamous Carcinoma','Squamous Carcinoma'),
            ('Adenosquamous Carcinoma','Adenosquamous Carcinoma'),
            ('Others','Others')
        ]),
        required=True
    )
    renew_other = forms.CharField(
        max_length=20, 
        help_text='Enter the Histological Cell Type if Others',
        label='Other Histological Type',
        required = False
    )
    renew_stage = forms.CharField(
        max_length=3,
        label='Stage of Disease',
        widget=forms.widgets.RadioSelect(choices=[('I','I'),('II','II'),('III','III'),('IV','IV')]),
        required=True
    )
    renew_status = forms.CharField(
        max_length=50,
        label='Treatment Status',
        widget=forms.widgets.RadioSelect(choices=[
            ('Treatment Naive','Treatment Naive'),
            ('On Chemotherapy','On Chemotherapy'),
            ('On Tyrosine Kinase Inhibitor(s)(TKI)','On Tyrosine Kinase Inhibitor(s)(TKI)')
        ]),
        required=True
    )
    renew_additional=forms.CharField(max_length=100, label='Additional Information',required=False)
    renew_request = forms.CharField(
        max_length=200,
        label='Request',
        widget=forms.widgets.RadioSelect(choices = (
            ("Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M","a) Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M"),
            ("#Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)","b) #Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)"),
            ("Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M + #Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)","a) + b)")
        )),
        required=True
    )

class Sortform(forms.Form):
    sortkey = forms.CharField(
        max_length=10,
        label='Sort the data by:',
        widget=forms.widgets.RadioSelect(choices=[('name','Name'),('id','ID')]),
        required=True
    )

class Searchform(forms.Form):
    searchkey = forms.CharField(
        max_length=10,
        label='Search data through:',
        widget=forms.widgets.RadioSelect(choices=[('name','Name'),('id','ID')]),
        required=True
    )
    searchvalue = forms.CharField(max_length=100, label='Search:')