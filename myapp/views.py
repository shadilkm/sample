from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnsample(request):
    return HttpResponse("hello")
def fnname(request):
    return render(request,"sample.html") 
