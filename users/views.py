from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NumDepartamentoForm
from .models import PagoComun, UserProfile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')



@login_required
def home(request):
    # Verificar si el usuario ya tiene un número de departamento
    user_profile = request.user.profile

    if request.method == 'POST':
        form = NumDepartamentoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir para evitar el reenvío del formulario
    else:
        form = NumDepartamentoForm(instance=user_profile)

    return render(request, 'users/home.html', {'form': form, 'user_profile': user_profile})