# Generated by Django 4.2 on 2023-06-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='quant_like',
            field=models.IntegerField(blank=True, default=0, verbose_name='Curtidas'),
        ),
    ]
