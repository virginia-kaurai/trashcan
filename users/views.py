from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>User registered successfully</h1>")
    else:
        form = RegisterForm()
        return render(request, 'registration.html', {'form': form})
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
