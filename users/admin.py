from django.contrib import admin
from .models import PagoComun, UserProfile
from django import forms
from django.contrib.auth.models import User  # Importar el modelo User

# Register your models here.
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
            # Asociar el pago con todos los usuarios con el mismo número de departamento
            usuarios = User.objects.filter(userprofile__num_departamento=obj.num_departamento)
            # Guardar primero el pago original (obj), para asegurarse de que tenga un ID asignado
            obj.save()  # Guardamos el primer pago para asignar un ID
            # Ahora crear un nuevo pago para cada usuario
            for usuario in usuarios:
                nuevo_pago = PagoComun(
                    monto=obj.monto,
                    descripcion=obj.descripcion,
                    mes_pago=obj.mes_pago,
                    num_departamento=obj.num_departamento,
                    usuario=usuario,
                    fecha_creacion=obj.fecha_creacion
                )
                nuevo_pago.save()  # Guardar la nueva instancia para cada usuario
        else:
            super().save_model(request, obj, form, change)  # Llamar al método original en caso de modificación

admin.site.register(PagoComun, PagoComunAdmin)
admin.site.register(UserProfile)