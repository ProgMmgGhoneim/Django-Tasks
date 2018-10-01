from django.urls import path ,include

from .views import UserCreate

urlpatterns = [
    path('', UserCreate),
]
