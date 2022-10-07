import datetime
from multiprocessing import context
import re
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 
from django.db.models import *

menu =[{'title':'Обращения','url_name': 'core:appeal'},
    {'title':'Заявители','url_name': 'core:applicant'},
    {'title':'Службы','url_name': 'core:emergency'}]


def number_of_incidents(request):
    incident = get_list_or_404(Appeal.objects)
    return HttpResponse("Количество происшествий - %s" % len(incident))



def telephone(request,pk):
    telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=pk)
    return HttpResponse(telephone)


def redirected(request,pk):
    return HttpResponseRedirect('/incidents/')


def inf(request):
    if request.GET:
        return HttpResponse(list(request.GET.dict().items()))


def applic_dict(request):
    tel = int(request.GET.get('tel'))
    applicant = Applicant.objects.filter(telephone=tel).values()
    return HttpResponse(applicant)

def applic_json(request,pk):
    applicant = get_object_or_404(Applicant, id=pk)
    data = model_to_dict(applicant, exclude='image')
    return JsonResponse(data)


def appeal(request):
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


def applicant(request):
    applicants = Applicant.objects.all()
    context = {
        'menu': menu,
        'title': 'Заявители', 
        'applicants': applicants
    }
    return render(request, 'core/application.html', context=context)

def emergency(request):
    emergencies = Emergency.objects.all()
    context = {
        'menu': menu,
        'title':'Службы', 
        'emergencies': emergencies
    }
    return render(request, 'core/emergency.html', context=context)   

def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request,'core/index.html', context=context)

def applicant_list(request):
    applicants_list = Applicant.objects.all()
    context = {
        'menu': menu,
        'title': 'Список заявителей', 
        'applicant_list': applicants_list
    }
    
    return render(request, 'core/applicant_list.html', context=context)

def appeal_list(request):
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