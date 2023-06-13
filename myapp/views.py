from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def work(request):
    return render(request,'work.html')

def work2(request):
    return render(request,'work2.html')

def work3(request):
    return render(request,'work3.html')

def work4(request):
    return render(request,'work4.html')

def work5(request):
    return render(request,'work5.html')
    
def work6(request):
    return render(request,'work6.html')

def works(request):
    return render(request,'works.html')
