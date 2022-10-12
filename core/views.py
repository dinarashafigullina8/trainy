import datetime
from multiprocessing import context
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 
from django.db.models import *
from django.views.generic.base import RedirectView 
from django.views.generic import ListView, TemplateView


class NumberOfIncidents(ListView):
    model = Appeal
    template_name = 'core/number_of_incidents.html'
    allow_empty = False
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incident'] = Appeal.objects.count()
        return context
    # def get(self, request):
    #     incident = get_list_or_404(Appeal.objects)
    #     return HttpResponse("Количество происшествий - %s" % len(incident))


class Telephone(ListView):
    model = Applicant
    template_name = 'core/telephone.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telephone'] = Applicant.objects.filter(id=self.kwargs['id']).values('telephone').first()['telephone']
        return context
    # def get(self,request,pk):
    #     telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=pk)
    #     return HttpResponse(telephone)

# class Redir(RedirectView):
    #def get(self,request,pk):
     #   return HttpResponseRedirect('/incidents/')

class Inf(View):

    # def get_context_data(self,request, **kwargs):
    #     if request.GET:
    #         context = super().get_context_data(**kwargs)
    #         context['inf'] = list(request.GET.dict().items())
    #         context['title'] = 'Инфромация'
    #     return context
    def get(self, request):
        if request.GET:
            return HttpResponse(list(request.GET.dict().items()))

class ApplicDict(View):
    def get(self,request):
        tel = request.GET.get('tel')
        applicant = Applicant.objects.filter(telephone=tel).values()
        return HttpResponse(applicant)

class ApplicJSON(View):
    def get(self,request,pk):
        applicant = get_object_or_404(Applicant, id=pk)
        data = model_to_dict(applicant, exclude='image')
        return JsonResponse(data)

class AppealView(ListView):
    model = Appeal
    
    template_name = 'core/appeal.html'
    context_object_name = 'appeals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обращения'
        context['n'] = datetime.datetime.now()
        context['avg_em'] = Appeal.objects.aggregate(Avg('emergency'))
        context['count_appeal'] = Appeal.objects.all().count()
        return context
    # def get(self, request):
    #     appeals = Appeal.objects.all()
    #     avg_em = Appeal.objects.aggregate(Avg('emergency'))
    #     sublist = Appeal.objects.values_list('number', 'emergency__name')
    #     count_appeal = Appeal.objects.all().count()
    #     now = datetime.datetime.now()
    #     context = {
    #     'menu': menu,
    #     'title' : 'Обращения',
    #     'appeals': appeals, 
    #     'avg_em': avg_em,
    #     'sublist': sublist,
    #     'count_appeal': count_appeal,
    #     'now' : now
    #     }
    #     return render(request, 'core/appeal.html', context=context)

class ApplicantView(ListView):
    model = Applicant
    template_name = 'core/application.html'
    context_object_name = 'applicants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявители'
        return context
    # def get(self, request):
    #     applicants = Applicant.objects.all()
    #     context = {
    #     'menu': menu,
    #     'title': 'Заявители', 
    #     'applicants': applicants
    #     }
    #     return render(request, 'core/application.html', context=context)

class EmergencyView(ListView):
    model = Emergency
    template_name = 'core/emergency.html'
    context_object_name = 'emergencies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Службы'
        return context
    # def get(self, request):
    #     emergencies = Emergency.objects.all()
    #     context = {
    #     'menu': menu,
    #     'title':'Службы', 
    #     'emergencies': emergencies
    #     }
    #     return render(request, 'core/emergency.html', context=context)   

class Index(TemplateView):
    template_name = 'core/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context 

    # def get(self,request):
    #     context = {
    #     'title': 'Главная страница'
    #     }
    #     return render(request,'core/index.html', context=context)

class ApplicantList(ListView):
    model = Applicant
    template_name = 'core/applicant_list.html'
    context_object_name = 'applicant_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заявителей'
        return context
    # def get(self,request):
    #     applicants_list = Applicant.objects.all()
    #     context = {
    #     'title': 'Список заявителей', 
    #     'applicant_list': applicants_list
    #     }
    #     return render(request, 'core/applicant_list.html', context=context)

class AppealList(ListView):
    model = Appeal
    template_name = 'core/appeal_list.html'
    context_object_name = 'appeal_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список происшествий'
        context['sublist'] = Appeal.objects.values_list('number', 'emergency__name')
        return context

    # def get(self,request):
    #     appeal_list = Appeal.objects.all()
    #     sublist = Appeal.objects.values_list('number', 'emergency__name')
    #     print(appeal_list)
    #     print(sublist)
    #     context = {
    #     'title': 'Список происшествий', 
    #     'appeal_list': appeal_list,
    #     'sublist': sublist
    #     } 
    #     return render(request, 'core/appeal_list.html', context=context)