# Generated by Django 4.2.6 on 2023-10-27 12:53

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_rename_auther_author_rename_authors_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=books.models.book_path),
        ),
    ]