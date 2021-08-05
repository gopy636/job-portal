from django.shortcuts import render,redirect
from appone.forms import *
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages,auth
from django.contrib.auth.mixins import LoginRequiredMixin
from appone.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class ShowHome(TemplateView):
    template_name="appone/home.html"


class UserRigistation(View):
    def get(self,request):
        form=UserRForm()
        return render(request,"appone/reg.html",{"form":form,"regist":True})
    def post(self,request):
        form=UserRForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request,'Registaion Sucessful please Log-in to continue')
            return render(request,"appone/home.html",{"form":form})
        return render(request,"appone/reg.html",{"form":form})



class Profile(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        if request.user.usertype=="Provider":
            user1=User.objects.get(username=request.user.username)
            try:
                p=Provider.objects.get(user=user1)
            except:
                p=None
            try:
                j=Job.objects.filter(provider=p)
            except :
                j=None
            if p==None:
                return redirect("/addp/")
            return render(request,"appone/profile.html",{"p":p,"job":j,"isProvider":True})
        if request.user.usertype=="Seeker":
            user1=User.objects.get(username=request.user.username)
            try:
                s=seeker.objects.get(user=user1)
            except Exception as e:
                s=None
            if s==None:
                return redirect("/addp/")
            try:
                j=Job.objects.filter(stream=s.looking_job_in)
            except Exception as e:
                j=None
            try:
                applied=s.job.all()
            except Exception as e:
                applied=None
            return render(request,"appone/profile.html",{"p":s,"job":j,"isSeeker":True,"applied":applied})
        return redirect("/index/")


class ProfileAdd(LoginRequiredMixin,View):
    login_url="/login/"
    def get(self,request):
        if request.user.usertype=="Provider":
            form=ProviderForm()
        if request.user.usertype=="Seeker":
            form=SeekerForm()
        return render(request,'appone/provider.html',{"form":form})

    def post(self,request):
        if request.user.usertype=="Provider":
            form=ProviderForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data.get("email")
                compyname=form.cleaned_data.get("compyname")
                Provider.objects.create(user=User.objects.get(username=request.user.username),
                                                            email=email,compyname=compyname)

        if request.user.usertype=="Seeker":
            print("*************in seeker post")
            form=SeekerForm(request.POST)
            if form.is_valid():
                looking_job_in=form.cleaned_data.get("looking_job_in")
                fname=form.cleaned_data.get("fname")
                lname=form.cleaned_data.get("lname")
                s=seeker(user=User.objects.get(username=request.user.username),
                                looking_job_in=looking_job_in,fname=fname,lname=lname)
                s.save()
        return redirect("/profile/")





class AddJob(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.usertype=="Provider":
            form=JobForm()
            return render(request,"appone/addjob.html",{"form":form})
        return redirect("/index/")
    def post(self,request):
        if request.user.usertype=="Provider":
            form=JobForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get("title")
                stream=form.cleaned_data.get("stream")
                desc=form.cleaned_data.get("desc")
                experence=form.cleaned_data.get("experence")
                date=form.cleaned_data.get("date")
                date_end=form.cleaned_data.get("date_end")
                p=Provider.objects.get(user=User.objects.get(username=request.user.username))
                Job.objects.create(title=title,stream=stream,desc=desc,
                                    experence=experence,date=date,date_end=date_end,provider=p)
        return redirect("/profile/")
