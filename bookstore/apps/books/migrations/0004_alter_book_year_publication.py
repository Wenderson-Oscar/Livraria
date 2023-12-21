# Generated by Django 4.2.3 on 2023-12-17 01:01

import bookstore.apps.books.models.book
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_publication',
            field=models.DateField(validators=[bookstore.apps.books.models.book.Book.validate_date], verbose_name='Ano de Publicação'),
        ),
    ]
