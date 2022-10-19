from dataclasses import fields
from email.mime import application
import django_filters
import django_filters.rest_framework
from core.models import Appeal, Applicant, Emergency

class AppealFilter(django_filters.FilterSet):
    pass



class ApplicantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name')
    telephone = django_filters.NumberFilter(field_name='telephone')
    birth = django_filters.DateFilter(field_name='birth', lookup_expr='icontains')
    class Meta:
        model = Applicant
        fields = ['name', 'telephone', 'birth']
    

class AppealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='application', method='name_filter')
    code = django_filters.NumberFilter(field_name='emergency')
    status = django_filters.CharFilter(field_name='status')

    def name_filter(self, queryset, name, value):
        return queryset.filter(application__name=value)

    class Meta:
        model = Appeal
        fields = ['code', 'status']