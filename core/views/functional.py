import datetime
from django.views.generic import View
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 
from django.db.models import *



def incidents(self, request):
    incident = get_list_or_404(Appeal.objects)
    return HttpResponse("Количество происшествий - %s" % len(incident))



def telephone(self,request,pk):
    telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=pk)
    return HttpResponse(telephone)


def redirect(self,request,pk):
    return HttpResponseRedirect('/incidents/')


def inf(self, request):
    if request.GET:
        return HttpResponse(list(request.GET.dict().items()))


def applic_dict(self,request):
    tel = request.GET.get('tel')
    applicant = Applicant.objects.filter(telephone=tel).values()
    return HttpResponse(applicant)


def applicJSON(self,request,pk):
    applicant = get_object_or_404(Applicant, id=pk)
    data = model_to_dict(applicant, exclude='image')
    return JsonResponse(data)

def appeal(self, request):
    appeals = Appeal.objects.all()
    avg_em = Appeal.objects.aggregate(Avg('emergency'))
    sublist = Appeal.objects.values_list('number', 'emergency__name')
    count_appeal = Appeal.objects.all().count()
    now = datetime.datetime.now()
    context = {
    'title' : 'Обращения',
    'appeals': appeals, 
    'avg_em': avg_em,
    'sublist': sublist,
    'count_appeal': count_appeal,
    'now' : now
    }
    return render(request, 'core/appeal.html', context=context)


def applicant(self, request):
    applicants = Applicant.objects.all()
    context = {
    'menu': menu,
    'title': 'Заявители', 
    'applicants': applicants
    }
    return render(request, 'core/application.html', context=context)


def emergency(self, request):
    emergencies = Emergency.objects.all()
    context = {
    'menu': menu,
    'title':'Службы', 
    'emergencies': emergencies
    }
    return render(request, 'core/emergency.html', context=context)    

def index(self,request):
    context = {
    'title': 'Главная страница'
    }
    return render(request,'core/index.html', context=context)


def applicant_list(self,request):
    applicants_list = Applicant.objects.all()
    context = {
    'title': 'Список заявителей', 
    'applicant_list': applicants_list
    }
    return render(request, 'core/applicant_list.html', context=context)



def appeal_list(self,request):
    appeal_list = Appeal.objects.all()
    sublist = Appeal.objects.values_list('number', 'emergency__name')
    print(appeal_list)
    print(sublist)
    context = {
    'title': 'Список происшествий', 
    'appeal_list': appeal_list,
    'sublist': sublist
    } 
    return render(request, 'core/appeal_list.html', context=context)