# Generated by Django 5.0.6 on 2024-12-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PagoComun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=255)),
                ('mes_pago', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pago Común',
                'verbose_name_plural': 'Pagos Comunes',
            },
        ),
    ]