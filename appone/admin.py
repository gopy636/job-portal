from django.contrib import admin
from appone.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Provider)
admin.site.register(seeker)
admin.site.register(Job)
