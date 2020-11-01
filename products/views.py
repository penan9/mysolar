from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Product, ProductDetail
import random
from aboutus.views import get_image


def index(request):
        products = Product.objects.all().order_by('date')
        last_entry = Product.objects.latest("date")
        last_date = last_entry.date
        for product in products:
            code = str(product.code)[0:4]
            if code != product.code2:
               product.code2 = code
               product.save()
        image1 = get_image("home")
        return render(request,'product.html', {'last_date': last_date, 'products':products, 'image1':image1})


def new(request):
        products = Product.objects.all().order_by('date')
        last_entry = Product.objects.latest("date")
        last_date = last_entry.date
        homepage = "welcome: "
        for product in products:
            code = str(product.code)[0:4]
            if code != product.code2:
               product.code2 = code
               product.save()
            homepage += product.code2
            homepage += " : "
            homepage += str(product.code)
            homepage += " ; "
#        return HttpResponse('New products ' + homepage)
        image1 = get_image("home")
        return render(request,'popup.html', {'image1':image1, 'last_date': last_date, 'products':products})


def sales(request):
	return HttpResponse('Products on sales!')


def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))


def details(request, p_id=0):
        id = format(p_id, '05d')
        print ("product details in view.py ID: " + id)
#        return HttpResponse('Products details ...' + id)
        image1 = get_image("home")
        try:
            products = Product.objects.filter(id=p_id)
            product_details = ProductDetail.objects.filter(productid=id)
            last_entry = product_details.latest("date")
            last_date = last_entry.date
        except ProductDetail.DoesNotExist:
            print ("Exception: DoesNotExist")
            print (ProductDetail)
            return HttpResponseRedirect('/products/new')
            return False
        return render(request,'product_details.html', {'last_date': last_date, 'products':products, 'product_details':product_details, 'image1':image1})
