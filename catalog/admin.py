from django.contrib import admin

# Register your models here.
from .models import Patients, Clinic_information

class PatientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'hkid', 'sex')

    fieldsets = (
        ('Specimen Collection (All * field must be filled)',{
            'fields':('specimen_type','other_type','collectiondate','collectiontime')
        }),

        ('Patient Information (All * field must be filled)',{
            'fields':('name','hkid', 'ethnicity','sex','dob')
        }),

        ('Referral site Information (All * field must be filled)',{
            'fields':('referral','clinicid','doctor','phone','fax','clinic')
        }),

        

    )
class ClinicAdmin(admin.ModelAdmin):
    list_display=('clinic_name',)
    fieldsets = (
        ('Clinic Information',{
            'fields':('clinic_name','previous','spid','diagnosis','celltype','other','stage','status','additional')
        }),

        ('Request*',{
            'fields':('request',)
        }),


    )

#admin.site.register(Patients)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(Clinic_information,ClinicAdmin)
