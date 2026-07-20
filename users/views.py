from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

from users.forms import RegisterForm
def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm()
        if RegisterForm.is_valid():
            RegisterForm.save()
            return HttpResponse("<h1>User registered successfully</h1>")
    else:
        form = RegisterForm()
        return render(request, 'registration.html', {'form': form})
