from django.shortcuts import render,redirect
from appone.forms import *
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages,auth
from django.contrib.auth.mixins import LoginRequiredMixin
from appone.models import *
from django.core.exceptions import ObjectDoesNotExist


class ShowApplicant(LoginRequiredMixin,View):
    def get(self,request,id):
        if request.user.usertype=="Provider":
            job=Job.objects.get(pk=id)
            sekr=seeker.objects.filter(job=job)
            print("*****",sekr)
        return render(request,"appone/showapplicant.html",{"seeker":sekr})
