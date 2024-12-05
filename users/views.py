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
    # Obtener el perfil del usuario actual
    user_profile = request.user.profile
    
    # Filtrar los pagos comunes para el departamento del usuario
    pagos_pendientes = PagoComun.objects.filter(num_departamento=user_profile.num_departamento)
    
    # Filtrar pagos ya realizados (esto depende de la estructura de tu modelo, por ejemplo, si tienes una fecha de pago)
    pagos_realizados = PagoComun.objects.filter(usuario=request.user, fecha_pago__isnull=False)
    
    # Manejar el formulario de número de departamento
    if request.method == 'POST':
        form = NumDepartamentoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir para evitar el reenvío del formulario
    else:
        form = NumDepartamentoForm(instance=user_profile)

    # Pasar los pagos y el formulario al contexto
    return render(request, 'users/home.html', {
        'form': form,
        'user_profile': user_profile,
        'pagos_pendientes': pagos_pendientes,
        'pagos_realizados': pagos_realizados
    })