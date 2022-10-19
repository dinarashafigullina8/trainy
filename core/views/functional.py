import datetime
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.forms import AddAppealForm
from core.models import Appeal, Applicant, Emergency
from django.forms.models import model_to_dict 
from django.db.models import *
from core.forms import AddAppealForm, AddApplicantForm, AddEmergencyForm
from core.filters import ApplicantFilter

def incidents(request):
    incident = get_list_or_404(Appeal.objects)
    return HttpResponse("Количество происшествий - %s" % len(incident))


def telephone(self,id):
    telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=id)
    return HttpResponse(telephone)


def redir(self,pk):
    return HttpResponseRedirect('/incidents/')


def inf(request):
    if request.GET:
        return HttpResponse(list(request.GET.dict().items()))


def applic_dict(request):
    tel = request.GET.get('tel')
    applicant = Applicant.objects.filter(telephone=tel).values()
    return HttpResponse(applicant)


def applicJSON(request,pk):
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
        'title' : 'Обращения',
        'appeals': appeals, 
        'avg_em': avg_em,
        'sublist': sublist,
        'count_appeal': count_appeal,
        'n' : now
    }
    return render(request, 'core/functional/appeal.html', context=context)


def applicant(request):
    applicants = Applicant.objects.all()
    context = {
        'title': 'Заявители', 
        'applicants': applicants
    }
    return render(request, 'core/functional/application.html', context=context)


def emergency(request):
    emergencies = Emergency.objects.all()
    context = {
        'title':'Службы', 
        'emergencies': emergencies
    }
    return render(request, 'core/functional/emergency.html', context=context)    


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request,'core/functional/index.html', context=context)


def applicant_list(request):
    applicants_list = Applicant.objects.all()
    context = {
        'title': 'Список заявителей', 
        'applicant_list': applicants_list
    }
    return render(request, 'core/functional/applicant_list.html', context=context)


def appeal_list(request):
    appeal_list = Appeal.objects.all()
    sublist = Appeal.objects.values_list('number', 'emergency__name')
    print(appeal_list)
    print(sublist)
    context = {
        'title': 'Список происшествий', 
        'appeal_list': appeal_list,
        'sublist': sublist
    } 
    return render(request, 'core/functional/appeal_list.html', context=context)


def add_appeal(request):
    if request.method == 'POST':
        form = AddAppealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = AddAppealForm()
    context = {
        'form' : form,
        'title' : 'Новое обращение'
    }
    return render(request, 'core/functional/add_appeal.html', context=context)


def add_applicant(request):
    if request.method == 'POST':
        form = AddApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = AddApplicantForm()
    context = {
        'form' : form,
        'title' : 'Новый заявитель'
    }
    return render(request, 'core/functional/add_applicant.html', context=context)


def add_emergency(request):
    if request.method == 'POST':
        form = AddEmergencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = AddEmergencyForm()
    context = {
        'form' : form,
        'title' : 'Новая служба'
    }
    return render(request, 'core/functional/add_emergency.html', context=context)



def search_applicant(request):
    f = ApplicantFilter(request.GET.name, queryset = Applicant.objects.all())
    return HttpResponse('core/functional/applicant.html', {'filter': f})