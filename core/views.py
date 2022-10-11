import datetime
from django.views.generic import View
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 
from django.db.models import *

menu =[{'title':'Обращения','url_name': 'core:appeal'},
    {'title':'Заявители','url_name': 'core:applicant'},
    {'title':'Службы','url_name': 'core:emergency'}]

class NumberOfIncidents(View):
    def get(self, request):
        incident = get_list_or_404(Appeal.objects)
        return HttpResponse("Количество происшествий - %s" % len(incident))


class Telephone(View):
    def get(self,request,pk):
        telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=pk)
        return HttpResponse(telephone)

class Redir(View):
    def get(self,request,pk):
        return HttpResponseRedirect('/incidents/')

class Inf(View):
    def get(self, request):
        if request.GET:
            return HttpResponse(list(request.GET.dict().items()))

class ApplicDict(View):
    def get(self,request):
        tel = int(request.GET.get('tel'))
        applicant = Applicant.objects.filter(telephone=tel).values()
        return HttpResponse(applicant)
class ApplicJSON(View):
    def get(self,request,pk):
        applicant = get_object_or_404(Applicant, id=pk)
        data = model_to_dict(applicant, exclude='image')
        return JsonResponse(data)

class AppealView(View):
    def get(self, request):
        appeals = Appeal.objects.all()
        avg_em = Appeal.objects.aggregate(Avg('emergency'))
        sublist = Appeal.objects.values_list('number', 'emergency__name')
        count_appeal = Appeal.objects.all().count()
        now = datetime.datetime.now()
        context = {
        'menu': menu,
        'title' : 'Обращения',
        'appeals': appeals, 
        'avg_em': avg_em,
        'sublist': sublist,
        'count_appeal': count_appeal,
        'now' : now
        }
        return render(request, 'core/appeal.html', context=context)

class ApplicantView(View):
    def get(self, request):
        applicants = Applicant.objects.all()
        context = {
        'menu': menu,
        'title': 'Заявители', 
        'applicants': applicants
        }
        return render(request, 'core/application.html', context=context)

class EmergencyView(View):
    def get(self, request):
        emergencies = Emergency.objects.all()
        context = {
        'menu': menu,
        'title':'Службы', 
        'emergencies': emergencies
        }
        return render(request, 'core/emergency.html', context=context)   

class Index(View):
    def get(self,request):
        context = {
        'menu': menu,
        'title': 'Главная страница'
        }
        return render(request,'core/index.html', context=context)

class ApplicantList(View):
    def get(self,request):
        applicants_list = Applicant.objects.all()
        context = {
        'menu': menu,
        'title': 'Список заявителей', 
        'applicant_list': applicants_list
        }
        return render(request, 'core/applicant_list.html', context=context)

class AppealList(View):
    def get(self,request):
        appeal_list = Appeal.objects.all()
        sublist = Appeal.objects.values_list('number', 'emergency__name')
        print(appeal_list)
        print(sublist)
        context = {
        'menu': menu,
        'title': 'Список происшествий', 
        'appeal_list': appeal_list,
        'sublist': sublist
        } 
        return render(request, 'core/appeal_list.html', context=context)