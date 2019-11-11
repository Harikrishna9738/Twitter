from django.contrib import admin
from .models import User, Tweet


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','password')


admin.site.register(User,UserAdmin)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet','date','user')


admin.site.register(Tweet,TweetAdmin)