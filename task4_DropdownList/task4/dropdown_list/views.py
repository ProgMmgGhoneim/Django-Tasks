from django.shortcuts import render
from django.views.generic import ListView , CreateView ,UpdateView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.

class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    template_name ='person_list.html'

class PersonCreate(CreateView):
    model = Person
    #fields =('name', 'birthday', 'country', 'city')
    form_class =PersonForm
    template_name ='person_form.html'
    success_url = reverse_lazy('person_list')

class PersonUpdate(UpdateView):
    model = Person
    #fields =('name', 'birthday', 'country', 'city')
    form_class =PersonForm
    template_name ='person_form.html'
    success_url = reverse_lazy('person_list')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
