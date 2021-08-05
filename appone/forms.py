from django import forms
from django.contrib.auth.forms import UserCreationForm
from appone.models import User

class UserRForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model=User
        fields=['usertype','username','password1',"password2","usertype",]

class ProviderForm(forms.Form):
    email=forms.EmailField()
    compyname=forms.CharField(max_length=20)

class SeekerForm(forms.Form):
    looking_job_in=forms.ChoiceField(choices=(("Mech","mech"),("Civil","civil"),("IT","IT")))
    fname=forms.CharField(max_length=20)
    lname=forms.CharField(max_length=20)


class JobForm(forms.Form):
    user_choices=(("Mech","mech"),("Civil","civil"),("IT","IT"))
    title=forms.CharField(max_length=20)
    stream=forms.ChoiceField(choices=user_choices)
    desc=forms.CharField(max_length=100)
    experence=forms.CharField()
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_end=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
