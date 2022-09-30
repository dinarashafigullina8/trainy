from django.contrib import admin
from core.models import *

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birth', 'telephone', 'health', 'image')
    list_editable = ('health', 'image')
    search_fields = ('name',)
    list_filter = ('gender',)
    empty_value_display = '*'

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'telephone')
    search_fields = ('name',)
    list_filter = ('code',)
    empty_value_display = '*'

class AppealAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'status','number_of_victims', 'dont_call')
    list_editable = ('status', 'dont_call')
    search_fields = ('status',)
    list_filter = ('status','dont_call')
    empty_value_display = '*'

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(Appeal, AppealAdmin)

