from django.db import models
from datetime import datetime,time


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(help_text="enter your email")
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Twitter(models.Model):
    tweet = models.TextField(help_text="enter you tweet")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)