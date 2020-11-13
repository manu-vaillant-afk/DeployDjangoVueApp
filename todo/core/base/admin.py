from django.contrib import admin
from .models import MyUser, Todo
from django.contrib.auth.admin import UserAdmin
# Register your models here.

my_models = [MyUser, Todo]

admin.site.register(my_models)


# admin.site.register(MyUser)
