from django.shortcuts import render,HttpResponse
from datetime import datetime
from TutorialsApp.models import Register
from django.contrib import messages

def index(request):
    context={
        'var' : 'this is sent'
    }
    return render(request,'index.html',context)

def services(request):
    return render(request,'services.html')

# Create your views here.

def about(request):
    return HttpResponse('This is my aboutpage')

def contact(request):
    #return render(request,'contact.html')
    return render(request,'contact.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=Register(name=name)
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'register.html')
