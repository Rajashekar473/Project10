from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from.modles import productapp
# Create your views here.
class productinput(View):
    def get(self,request):
        return render(request,'productapp.html')
class inputdata(View):
    def get(self,request):
        x=int(request.GET["t1"])
        y=request.GET["t2"]
        z=float(request.GET["t3"])
        p=request.GET["t4"]
        q=request.GET["t5"]
        p1=product(pid=x,pname=y,pcost=z,pmfdt=p,pexpdt=q)
        p1.save()
        return HttpResponse("data sucessfully saved")
