from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from letslearn.models import Home
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("My name is Enzo")
def say(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render()
                        )
def index(request):
    myhome = Home.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request)) 

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    a = request.POST['email']
    b = request.POST['mobileno']
    c = request.POST['age']
    home = Home(firstname=x, lastname=y, email_id=a, mobileno=b, age=c)
    home.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    home = Home.objects.get(id=id)
    home.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    myhome = Home.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myhome': myhome,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    mobileno = request.POST['mobileno']
    age = request.POST['age']
    home = Home.objects.get(id=id)
    home.firstname = first
    home.lastname = last
    home.email_id = email
    home.mobileno = mobileno
    home.age = age
    home.save()
    return HttpResponseRedirect(reverse('index'))
    