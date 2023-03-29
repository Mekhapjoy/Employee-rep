from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from.models import*

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def addemployee(request):
    if request.method=="POST":
        uname=request.POST['empname']
        eid=request.POST['emaill']
        address1=request.POST['address']
        desig=request.POST['dg']
        img2=request.POST['img1']
        employee(username=uname,email=eid,address=address1,designation=desig,image=img2).save()
        return redirect(index)

    return render(request,'addemployee.html')
def viewemployee(request):
    e=employee.objects.all()
    d1={'key1':e}
    return render(request,'viewemployee.html',d1)
def updateemployee(request,z):
    s=employee.objects.get(id=z)
    if request.method=="POST":
        s.username=request.POST["n1"]
        s.email=request.POST["n2"]
        s.address=request.POST["n3"]
        s.image=request.POST["n4"]
        s.designation=request.POST["n5"]
        s.save()
        return redirect(viewemployee)
    return render(request,'updateemployee.html',{'uekey':s})
def deleteemployee(request,pk):
    store=employee.objects.get(id=pk)
    store.delete()
    return redirect(viewemployee)
    
