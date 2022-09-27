from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from core.models import *
from django.views.generic import View
from django.shortcuts import redirect
from django.forms.models import model_to_dict 


def number_of_incidents(request):
    incident = Appeal.objects.count()
    if incident == 0:
        raise Http404("Происшествий нет")
    return HttpResponse("Количество происшествий - %s" % incident)



class ApplicantDetail(View):
    def get(self, request, id):
        if int(id) > Applicant.objects.count():
            return redirect('/incidents/', permanent=False)
        telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=id)
        return HttpResponse(telephone)

def inf(request):
    if request.GET:
        return HttpResponse(list(request.GET.dict().items()))


def applic_dict(request):
    tel = int(request.GET.dict()['tel'])
    applicant = Applicant.objects.filter(telephone=tel).values()
    return HttpResponse(applicant)

def applic_json(request):
    tel = int(request.GET.dict()['tel'])
    applicant = Applicant.objects.filter(telephone=tel).values()
    applicant = list(applicant)
    applicant = JsonResponse(applicant, safe=False)
    return HttpResponse(applicant.content)


    

