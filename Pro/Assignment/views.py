# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Note


def home(request):
    return render(request,"base.html",{})


def store(request):
    obj=Note()
    msg=request.POST.get('textmsg')
    if msg==" " or msg==None:
        pass
    else:
        obj.msg=msg
        obj.save()
    return render(request,"base.html",{})

def edit(request,id):
    obj=Note.objects.get(id=id)
    return render(request,'editcreate.html',{'yes':True,'data':obj})


def updateNote(request,id):
    obj=Note.objects.get(id=id)
    msg=request.POST.get('textmsg')
    obj.msg=msg
    obj.save()
    return redirect('view12')
    #return render(request,'editcreate.html',{'data':obj})


def deleted(request,id):
    obj=Note.objects.get(id=id)
    obj.delete()
    return redirect('view12')
    return render(request,'data.html',{})



def view12(request):
    data1=Note.objects.all()
    return render(request,"data.html",{'data':data1})

def front(request):
    return render(request,'front.html',{})
