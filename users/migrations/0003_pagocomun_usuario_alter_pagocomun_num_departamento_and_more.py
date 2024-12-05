# Generated by Django 5.0.6 on 2024-12-05 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pagocomun_num_departamento_userprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pagocomun',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagocomun',
            name='num_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='num_departamento',
            field=models.CharField(blank=True, default='Desconocido', max_length=10, null=True),
        ),
    ]
