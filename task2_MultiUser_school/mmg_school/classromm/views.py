from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import *
# Create your views here.
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeachetSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')
