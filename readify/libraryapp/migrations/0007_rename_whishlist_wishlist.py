# Generated by Django 4.2.4 on 2023-09-11 06:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryapp', '0006_whishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='whishlist',
            new_name='Wishlist',
        ),
    ]