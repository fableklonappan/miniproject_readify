# Generated by Django 4.2.4 on 2023-09-12 07:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryapp', '0008_rename_book_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='BookCart',
        ),
    ]
