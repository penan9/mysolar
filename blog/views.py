import os
from os.path import abspath, isfile
from django.http import HttpResponse
from django.shortcuts import render
from aboutus.models import About
from aboutus.views import get_image
from home.models import Home


def read_more(request):
    about1 = About.objects.all().order_by('sequence')
    home1 = Home.objects.all()
    image1 = get_image("home")
#    for myAbout in about1:
#        homepage = myAbout.name
#        homepage += myAbout.body
#    return HttpResponse('New products '+homepage)
    return render(request,'read_more.html', {'image1':image1, 'about1':about1, 'home1':home1})
