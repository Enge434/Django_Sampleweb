from django.db import models

from django.urls import reverse

# Create your models here.

class Patients(models.Model):
    
    specimen_type = models.CharField(max_length=20,choices=(('Blood','Blood'),('Pleural Fluid','Pleural Fluid'),('others','Others')),blank=True,verbose_name="Specimen Type *")

    other_type = models.CharField(max_length=30, help_text="If you choose others, please state:", blank=True)

    collectiondate = models.CharField(max_length=20,verbose_name="Collection Date *")

    collectiontime = models.CharField(max_length = 5, help_text="HH:MM" ,verbose_name="Collection Time *")

    name = models.CharField(max_length=30, help_text="Enter the patient's name", verbose_name='Full Name *')

    hkid = models.CharField(max_length=20, help_text="Enter the patient's HKID/Passport No.",verbose_name="HKID/National ID/Passport ID *")

    ethnicity = models.CharField(max_length=20, help_text="Enter the patient's Ethnicity",blank = True,verbose_name='Ethnicity ')

    sex = models.CharField(max_length=20, help_text="Enter the patient's sex", verbose_name='Sex *',choices=(('F','F'),('M','M'),('Prefer not to say','Prefer not to say')),blank=True)

    dob = models.CharField(max_length=20,verbose_name="Date of Birth *")

    referral = models.CharField(max_length=20, help_text="Enter the Referral Site", verbose_name="Referral Site *")

    clinicid = models.CharField(max_length=10, help_text = "Enter the Clinic ID",blank = True)

    doctor = models.CharField(max_length=30, help_text = "Enter the Referral Doctor", verbose_name="Referral Doctor *")

    phone = models.CharField(max_length=15, help_text="Enter the phone number",blank = True)

    fax = models.CharField(max_length=30, help_text='Enter the fax number', blank = True)

    clinic = models.ForeignKey('Clinic_information',on_delete=models.SET_NULL, null = True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('patients-detail', args=[str(self.id)])
    


class Clinic_information(models.Model):

    clinic_name = models.CharField(max_length=20, help_text="Enter the patient's name", verbose_name="Patient Name:",primary_key=True)

    previous = models.CharField(max_length = 3, choices=(('Yes','Yes'),('No','No')), default='N/A', help_text="Has patient preformed p-EGFR test in Sanomics previously?")

    spid = models.CharField(max_length=10, help_text = "If yes, Enter the patient's Sanomics Patient ID", blank=True)

    diagnosis = models.CharField(max_length=10, choices=(('Confirmed','Confirmed'),('Pending','Pending')), help_text="Diagnosis of Lund Cancer:", blank = True)

    celltype = models.CharField(max_length=30, choices=(('Adenocarcinoma','Adenocarcinoma'),('Squamous Carcinoma','Squamous Carcinoma'),('Adenosquamous Carcinoma','Adenosquamous Carcinoma'),('Others','Others')), help_text="If confirmed, Histological Cell Type:", blank = True)

    other = models.CharField(max_length=30, help_text="If choose others, please state:", blank = True)

    stage = models.CharField(max_length=5, choices = (('I','I'),('II','II'),('III','III'),('IV','IV')), verbose_name="Stage of Disease",blank = True)

    status = models.CharField(max_length=100, choices=(('Treatment Naive','Treatment Naive'),('On Chemotherapy','On Chemotherapy'),('On Tyrosine Kinase Inhibitor(s)(TKI)','On Tyrosine Kinase Inhibitor(s)(TKI)')),verbose_name="Treatment Status",blank=True)

    additional = models.CharField(max_length=100, verbose_name="Additional Information", blank = True,default='')

    request = models.CharField(max_length=200, choices = (
        ("Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M","a) Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M"),
        ("#Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)","b) #Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)"),
        ("Exon 19 Deletions + Exon 21 L858R + Exon 20 T790M + #Exon 20 C797S(Test for resistance to T790M-targeting EGFR TKI)","a) + b)")
    ),blank=True, help_text="Remarks: TWO Streck tubes of specimen are required for a) OR a) + b)\n         ONE Streck tuve of specimen is required for b) only")

    
    






