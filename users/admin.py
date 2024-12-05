from django.contrib import admin
from .models import PagoComun, UserProfile
from django import forms
from django.contrib.auth.models import User  # Importar el modelo User

# Formulario de PagoComun para agregar la selección de número de departamento desde los perfiles de usuario
class PagoComunForm(forms.ModelForm):
    class Meta:
        model = PagoComun
        fields = ['monto', 'descripcion', 'mes_pago', 'num_departamento', 'usuario']

    # Modificar el campo num_departamento para que sea una lista de los perfiles de usuario
    num_departamento = forms.ModelChoiceField(queryset=UserProfile.objects.all(), empty_label="Seleccionar Departamento")
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Seleccionar Usuario")

class PagoComunAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'mes_pago', 'num_departamento', 'fecha_creacion', 'usuario')
    list_filter = ('mes_pago', 'num_departamento')
    search_fields = ('descripcion',)

    # Agregar opción de asignar número de departamento al crear pago
    def save_model(self, request, obj, form, change):
        if not change:  # Solo cuando se crea el objeto
            # Asocia el pago con todos los usuarios con el mismo número de departamento
            usuarios = User.objects.filter(userprofile__num_departamento=obj.num_departamento)
            for usuario in usuarios:
                # Asociamos el pago con el usuario correspondiente
                obj.usuario = usuario  # Establecer el usuario
                obj.pk = None  # Crear una nueva instancia del pago
                obj.save()  # Guardar la nueva instancia
        else:
            super().save_model(request, obj, form, change)  # Llamar al método original en caso de modificación

admin.site.register(PagoComun, PagoComunAdmin)
admin.site.register(UserProfile)
