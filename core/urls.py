from django.urls import path, include

from core.views import *

app_name = 'core'
urlpatterns = [
    path('', index),
    path('incidents/', number_of_incidents, name='incidents'),
    path('telephone/<int:pk>/', telephone, name='telephone'),
    path('<int:pk>/', redirected,name='redir'),
    path('inf/', inf, name='inf'),
    path('applic/', applic_dict, name='applic'),
    path('applicJ/<int:pk>/', applic_json, name='applicJ'),
    path('appeal/', appeal, name='appeal'),
    path('emergency/', emergency, name='emergency'),
    path('applicant/', applicant, name='applicant'),
    path('a_list/', applicant_list, name='applicant_list'),
    path('appeal_list/', appeal_list, name='appeal_list')
]