from django.shortcuts import render,redirect

from .forms import UserForm

# Create your views here.
def UserCreate(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserForm()
    return render(request, 'form_save.html', {'form': form})
