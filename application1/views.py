from django.shortcuts import render
from django.http import HttpResponse
from application1.models import Registerdata
from application1.forms import Registerform

def home(request):
    return render(request, 'apps/home.html')

def show(request):
    stu=Registerdata.objects.all()
    return render(request, 'apps/show.html',{'s':stu})

def add(request):
    form=Registerdata()
    if request.method=="POST":
        form=Registerdata(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'apps/add.html',{'form':form} )
        
        
