from urllib import request
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def civil_work(request):
    return render(request,'civil_works.html')
    