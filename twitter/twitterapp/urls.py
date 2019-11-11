from django.urls import path,include
from .views import *



from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User',views.UserView)
router.register('Tweet',views.TweetView)


urlpatterns = [
    path('',api_user_details_view,name ='user_details'),
    path('user/',api_user_update_view,name ='user_update',),

]