# Generated by Django 4.2 on 2023-06-15 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='id_response',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='response',
        ),
        migrations.AddField(
            model_name='chat',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='chat.chat'),
        ),
    ]
