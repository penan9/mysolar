from django.http import HttpResponse
from django.shortcuts import render
from .models import Procedure
import copy
import random
from aboutus.views import get_image


def procedure_list(request):
    procedures = Procedure.objects.all().order_by('date');
    image1 = get_image("home")
    return render(request, 'procedure/procedure_list.html', { 'procedures': procedures, 'image1':image1 })


def procedure_code(request, p_code="C101"):
    procedures = Procedure.objects.all().order_by('date');
    procedure1 = Procedure();
    homepage = ""
    for myProcedure in procedures:
        if p_code == myProcedure.code:
            homepage = "welcom"
            procedure1 = copy.copy(myProcedure)
    image1 = get_image("home")
#    return HttpResponse('New procedure code: '+homepage + procedure1.code)
    return render(request, 'procedure/procedure_list.html', { 'procedure1': procedure1, 'image1':image1 })


def procedure_err(request, homepage):
    return HttpResponse('procedure: '+homepage)
