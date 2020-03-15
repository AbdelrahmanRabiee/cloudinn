from django.urls import path

from rest_framework import routers

from empires.views import index
from empires.viewsets import UnitViewsets

app_name='empires'
urlpatterns = [
        path('',index,name='index'),
        ]


unit_router = routers.SimpleRouter()
unit_router.register(r'unit', UnitViewsets)