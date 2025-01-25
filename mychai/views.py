from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def types_of_chai(request):
    return render(request,'mychai/index.html')

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'mychai/index.html',{'chais':chais})
