"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^procedures/', include('procedures.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^', include('home.urls')),
    url(r'^read_more$', views.read_more),
    url(r'^products/', include('products.urls')),
    url(r'^products/new', include('products.urls')),
    url(r'^products/sales', include('products.urls')),
    url(r'^products/details', include('products.urls')),
    url(r'^sendemail/', include('sendemail.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
admin.site.index_title = "Welcome to Kemuning Oil & Gas Portal"
