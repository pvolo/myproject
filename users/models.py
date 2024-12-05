from django.db import models
from django.contrib.auth.models import User

class PagoComun(models.Model):
    MESES = [
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    ]

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    mes_pago = models.CharField(max_length=10, choices=MESES)  # Cambiado a 10
    num_departamento = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # Asociamos al UserProfile
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descripcion} - {self.mes_pago}"

    class Meta:
        verbose_name = 'Pago Común'
        verbose_name_plural = 'Pagos Comunes'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_departamento = models.CharField(max_length=10, default='Desconocido', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.num_departamento}"

# Relacionamos el "UserProfile" a los usuarios
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
