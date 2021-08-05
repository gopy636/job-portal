from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from jobportal import settings

class User(AbstractUser):

    user_choice =(
        ('Provider','provider'),
        ('Seeker','seeker'),
        )
    usertype = models.CharField(max_length = 30, choices = user_choice,default = "Seeker",)

    def __str__(self):
        return self.username

class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email=models.EmailField()
    compyname=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username



class Job(models.Model):
    user_choices=(("Mech","mech"),("Civil","civil"),("IT","IT"))
    title=models.CharField(max_length=20)
    stream=models.CharField(max_length=10,choices  =user_choices,default="IT")
    desc=models.TextField(max_length=100)
    experence=models.CharField(max_length=20,null=True)
    date=models.DateField(default = datetime.date.today)
    date_end=models.DateField()
    provider=models.ForeignKey(Provider,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class seeker(models.Model):
    user_choices=(("Mech","mech"),("Civil","civil"),("IT","IT"))
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    looking_job_in=models.CharField(max_length=20,choices=user_choices,default="IT")
    job=models.ManyToManyField(Job)
    def __str__(self):
        return self.user.username
