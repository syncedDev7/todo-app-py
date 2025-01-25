from django.http import HttpResponse
from django.shortcuts import render 

def home_page(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html")

def about(request):
    # return HttpResponse("this is about page")
    return render(request,"website/index.html")

def contact(request):
    return HttpResponse("this is contact page")