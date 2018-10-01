from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', PersonList.as_view(), name ='person_list'),
    path('add/', PersonCreate.as_view(), name ='person_add'),
    path('<int:pk>/', PersonUpdate.as_view(), name ='person_update'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),  # <-- this one here


]
