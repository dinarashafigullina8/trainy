from django.urls import path

from core.views import *

app_name = 'core'
urlpatterns = [
    path('', Index.as_view()),
    path('incidents/', NumberOfIncidents.as_view(), name='incidents'),
    path('telephone/<int:pk>/', Telephone.as_view(), name='telephone'),
    path('<int:pk>/', Redir.as_view(),name='redir'),
    path('inf/', Inf.as_view(), name='inf'),
    path('applic/', ApplicDict.as_view(), name='applic'),
    path('applicJ/<int:pk>/', ApplicJSON.as_view(), name='applicJ'),
    path('appeal/', AppealView.as_view(), name='appeal'),
    path('emergency/', EmergencyView.as_view(), name='emergency'),
    path('applicant/', ApplicantView.as_view(), name='applicant'),
    path('a_list/', ApplicantList.as_view(), name='applicant_list'),
    path('appeal_list/', AppealList.as_view(), name='appeal_list')
]