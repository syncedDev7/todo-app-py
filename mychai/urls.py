from django.contrib import admin
from django.urls import path
from . import views #current directory se views ko import karo 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.types_of_chai,name='types_of_chai'),
    path('order/',views.all_chai,name='all_chai')
]