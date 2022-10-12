from django.urls import path

from core.views.functional import *

app_name = 'core'
urlpatterns = [
    path('', index),
    path('incidents/', incidents, name='incidents'),
    path('telephone/<int:id>/', telephone, name='telephone'),
    path('incidents/<int:pk>/', redirect,name='redir'),
    path('inf/', inf, name='inf'),
    path('applic/', applic_dict, name='applic'),
    path('applicJ/<int:pk>/', applicJSON, name='applicJ'),
    path('appeal/', appeal, name='appeal'),
    path('emergency/', emergency, name='emergency'),
    path('applicant/', applicant, name='applicant'),
    path('a_list/', applicant_list, name='applicant_list'),
    path('appeal_list/', appeal_list, name='appeal_list')
]