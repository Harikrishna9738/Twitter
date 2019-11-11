from rest_framework import serializers
from .models import *

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','password')



class TweetSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweet','date','user')




