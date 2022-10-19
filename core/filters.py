import django_filters
import django_filters.rest_framework
from core.models import Appeal, Applicant, Emergency

class AppealFilter(django_filters.FilterSet):
    pass



class ApplicantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name')
    class Meta:
        model = Appeal
        fields = '__all__'
    
