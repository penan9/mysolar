from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.procedure_list),
    path('<slug:p_code>/', views.procedure_code),
]
