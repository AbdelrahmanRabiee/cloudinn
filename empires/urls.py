from django.urls import path
from empires.views import index

app_name='empires'
urlpatterns = [
        path('',index,name='index'),
        ]