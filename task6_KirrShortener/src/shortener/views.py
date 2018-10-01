from django.shortcuts import render ,reverse ,get_object_or_404
from django.views import View

from .forms import KirrSubmit
from .models import KirURLModel
# Create your views here.
def Home(request ,*args ,**kwarg):
    if request.method == 'POST':
        form = KirrSubmit(request.POST)
        if form.is_valid():
            url = form.cleaned_data['Url']
            obj , create = KirURLModel.objects.get_or_create(Url=url)
            context ={
            'form':form,
            'object':obj,
            'create':create
            }
            return render(request , 'kirr/home.html',context=context)
    else:
        form = KirrSubmit()
    return render(request , 'kirr/home.html',{'form':form})
