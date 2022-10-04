from multiprocessing import context
import re
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 

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
    return render(request, 'core/appeal.html', {'title' : 'Обращения','appeals': appeals})


def applicant(request):
    applicants = Applicant.objects.all()
    return render(request, 'core/application.html', {'title': 'Заявители', 'applicants': applicants})

def emergency(request):
    emergencies = Emergency.objects.all()
    return render(request, 'core/emergency.html', {'title':'Службы', 'emergencies': emergencies})   

def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request,'core/base.html', context=context)

