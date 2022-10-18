import datetime
from multiprocessing import context
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 
from django.db.models import *
from django.views.generic.base import RedirectView 
from django.views.generic import ListView, TemplateView, CreateView
from core.forms import AddAppealForm, AddApplicantForm, AddEmergencyForm


class NumberOfIncidents(ListView):
    model = Appeal
    template_name = 'core/class_based/number_of_incidents.html'
    allow_empty = False
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incident'] = Appeal.objects.count()
        return context


class Telephone(ListView):
    model = Applicant
    template_name = 'core/class_based/telephone.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telephone'] = Applicant.objects.filter(id=self.kwargs['id']).values('telephone').first()['telephone']
        return context


class Redir(RedirectView):
    pattern_name = 'core/class_based/:index'


class Inf(View):
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
    
    template_name = 'core/class_based/appeal.html'
    context_object_name = 'appeals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обращения'
        context['n'] = datetime.datetime.now()
        context['avg_em'] = Appeal.objects.aggregate(Avg('emergency'))
        context['count_appeal'] = Appeal.objects.all().count()
        return context


class ApplicantView(ListView):
    model = Applicant
    template_name = 'core/class_based/application.html'
    context_object_name = 'applicants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявители'
        return context


class EmergencyView(ListView):
    model = Emergency
    template_name = 'core/class_based/emergency.html'
    context_object_name = 'emergencies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Службы'
        return context  


class Index(TemplateView):
    template_name = 'core/class_based/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context 


class ApplicantList(ListView):
    model = Applicant
    template_name = 'core/class_based/applicant_list.html'
    context_object_name = 'applicant_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заявителей'
        return context


class AppealList(ListView):
    model = Appeal
    template_name = 'core/class_based/appeal_list.html'
    context_object_name = 'appeal_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список происшествий'
        context['sublist'] = Appeal.objects.values_list('number', 'emergency__name')
        return context


class AddAppeal(CreateView):
    form_class = AddAppealForm
    template_name = 'core/class_based/add_appeal.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление обращения'
        return context

class AddApplicant(CreateView):
    form_class = AddApplicantForm
    template_name = 'core/class_based/add_applicant.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление заявителя'
        return context


class AddEmergency(CreateView):
    form_class = AddEmergencyForm
    template_name = 'core/class_based/add_emergency.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление службы'
        return context