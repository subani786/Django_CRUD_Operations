
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . forms import Studentform
from . models import Student
from django.contrib import messages
# Create your views here.



def addandshow(request):
    if request.method =="POST":
        fm=Studentform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You are succesfully added student ')
       # nm=fm.cleaned_data['name']
       # em=fm.cleaned_data['email']
       # ps=fm.cleaned_data['password']
       #     temp=Student(name='nm',email='em',password='ps')

            fm=Studentform()
    else:
        fm=Studentform()
    temp=Student.objects.all()
    return render(request,'main/addandshow.html',{'form':fm,'values':temp})


def studdelete(request,id):
    if request.method =='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        messages.warning(request,"Deleted successfully!")
        return HttpResponseRedirect('/')


def editstu(request,id):
    if request.method =='POST':
        pi=Student.objects.get(pk=id)
        fm=Studentform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You are successfully updated.')
    else:
        pi=Student.objects.get(pk=id)
        fm=Studentform(instance=pi)
    return render(request,'main/editupdate.html',{'form':fm})






