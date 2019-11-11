from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerialiser
    queryset = User.objects.all()

class TweetView(viewsets.ModelViewSet):
    serializer_class = TweetSerialiser
    queryset = Tweet.objects.all()

@api_view(['GET',])
def api_user_details_view(request):
    name = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerialiser(name  , many=True)
    return Response(serializer.data)


@api_view(['PUT',])
def api_user_update_view(request,pk):
    if request.method == 'PUT':
        try:
            name = User.objects.get(password= pk)
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        else:

            serializer = UserSerialiser(name  , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_200_OK)
            return Response(status.HTTP_400_BAD_REQUEST)
