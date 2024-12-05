from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NumDepartamentoForm
from .models import PagoComun, UserProfile
from django.shortcuts import get_object_or_404


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

    # Filtrar los pagos relacionados con el usuario y su número de departamento
    pagos = PagoComun.objects.filter(usuario=request.user, num_departamento__num_departamento=user_profile.num_departamento)
    print("Pagos encontrados: ", pagos)  # Esto imprimirá el queryset de los pagos en la consola

    if request.method == 'POST':
        form = NumDepartamentoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir para evitar el reenvío del formulario
    else:
        form = NumDepartamentoForm(instance=user_profile)

    return render(request, 'users/home.html', {
        'form': form,
        'user_profile': user_profile,
        'pagos': pagos
    })
    
    
    
@login_required
def realizar_pago(request, pago_id):
    # Obtener el pago correspondiente
    pago = get_object_or_404(PagoComun, id=pago_id, usuario=request.user)

    if request.method == 'POST':
        # Simular el pago (en este caso, simplemente marcarlo como pagado)
        data_boleta = {
            'descripcion': pago.descripcion,
            'monto': pago.monto,
            'mes_pago': pago.mes_pago,
            'num_departamento': pago.num_departamento,
        }

        # Eliminar el pago de la colección `PagoComun`
        pago.delete()

        # Pasar la información del pago a la plantilla de la boleta
        return render(request, 'users/boleta.html', data_boleta)

    return render(request, 'users/realizar_pago.html', {'pago': pago})  


