from django.http import HttpResponse
from django.shortcuts import render
from .models import About
import random
from home.models import Image


def get_image(request):
    image = Image.objects.all()
    image1 = Image()
    homepage = "aboutus"
    try:
        myimage = []
        for myimage1 in image:
            if (myimage1.directory == request):
                myimage.append(myimage1.file)
        image1.file =random.choice(myimage)
#        assert False, myimage
    except IndexError:
        homepage += " - Error: IndexError"
        print (homepage)
    else:
        if image1:
            homepage += str(image1.file)
    return(image1)
         

def index(request):
    about1 = About.objects.all().order_by('sequence')
    image1 = get_image("home")
    return render(request,'about.html', {'about1':about1, 'image1':image1})
