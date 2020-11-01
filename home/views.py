from django.http import HttpResponse
from django.shortcuts import render
from .models import Home
from aboutus.models import About
from aboutus.views import get_image
import random


def index(request):
    about1 = About.objects.all().order_by('sequence')
    home = Home.objects.all()
    image2 = get_image("hp")
#    home2 = Home.objects.values()
#    assert False, home
#    assert False, home2
    home1 = Home()
    homepage = "home: "
    try:
        myhomes = []
        for myhome in home:
            myhomes.append(myhome.file) 
        home1.file =random.choice(myhomes) 
    except IndexError:
        homepage += " Error: IndexError" 
        print (homepage)
    else:
        if home1:
            homepage += str(home1.file)
 #   returnHttpResponse(homepage)
    return render(request, 'index.html', { 'home1': home1, 'about1' : about1, 'image2' : image2})
