# Generated by Django 4.2.4 on 2023-09-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0012_pdfbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfbook',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='book_pdfs/'),
        ),
    ]
