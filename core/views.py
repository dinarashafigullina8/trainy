from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from core.models import *
from django.forms.models import model_to_dict 


def number_of_incidents(request):
    incident = get_list_or_404(Appeal.objects)
    return HttpResponse("Количество происшествий - %s" % len(incident))



def telephone(request,id):
    telephone = get_object_or_404(Applicant.objects.values_list('telephone',), id__iexact=id)
    return HttpResponse(telephone)


def redirected(request,id):
    return HttpResponseRedirect('/incidents/')


def inf(request):
    if request.GET:
        return HttpResponse(list(request.GET.dict().items()))


def applic_dict(request):
    tel = int(request.GET.get('tel'))
    applicant = Applicant.objects.filter(telephone=tel).values()
    return HttpResponse(applicant)

def applic_json(request,id):
    applicant = get_object_or_404(Applicant, id=id)
    data = model_to_dict(applicant, exclude='image')
    return JsonResponse(data)


    

