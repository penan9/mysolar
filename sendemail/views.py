# sendemail/views.py
import sqlite3
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactFormModel
import random
from aboutus.views import get_image

#conn = sqlite3.connect("db.sqlite3")
#c = conn.cursor()
#c.close()
#conn.close()


#def data_entry():
#    c.execute("INSERT INTO 


def index(request):
    image1 = get_image("home")
    if request.method == 'GET':
        form = ContactForm()
    else:
        contactformmodels = ContactFormModel.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            to_email = ['kemuning2021@gmail.com']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            to_email.append(form.cleaned_data['email'])
            message = "\nSent by: "
            message += from_email
            message += "\n\n"
            message += form.cleaned_data['message']
            message += "\n\n------------\n\nFrom Kemuning Oil & Gas."
            try:
                send_mail(subject, message, from_email, to_email)
            except OSError:
                return HttpResponse('Network busy, please try again...')
            for contactformmodel in contactformmodels:
                return HttpResponse("ok..")
            return render(request, "success.html", {'form': form, 'image1':image1})
    return render(request, "email.html", {'form': form, 'image1':image1})
