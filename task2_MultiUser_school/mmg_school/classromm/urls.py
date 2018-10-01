from django.urls import path ,include

from .views import TeacherSignUpView
urlpatterns = [
    path('signup' ,TeacherSignUpView.as_view())
]
