from django.contrib import admin
from .models import User, Twitter


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','password')


admin.site.register(User,UserAdmin)


class TwitterAdmin(admin.ModelAdmin):
    list_display = ('tweet','date','user')


admin.site.register(Twitter,TwitterAdmin)