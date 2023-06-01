# Generated by Django 4.2 on 2023-06-01 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.ImageField(blank=True, upload_to='', verbose_name='Foto de Perfil')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'MASCULINO'), ('F', 'FEMENINO'), ('O', 'OUTROS')], max_length=1)),
                ('data_entrada', models.DateTimeField(auto_now_add=True, verbose_name='Date de Criação da Conta')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
