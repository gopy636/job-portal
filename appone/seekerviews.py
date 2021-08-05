from django.shortcuts import render,redirect
from appone.forms import *
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages,auth
from django.contrib.auth.mixins import LoginRequiredMixin
from appone.models import *
from django.core.exceptions import ObjectDoesNotExist


class JobApply(LoginRequiredMixin,View):
    def get(self,request,id):
        if request.user.usertype=="Seeker":
            s=seeker.objects.get(user=request.user)
            s.job.add(Job.objects.get(pk=id))
            s.save()
        return redirect("/profile/")
