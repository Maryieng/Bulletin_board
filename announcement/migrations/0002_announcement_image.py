# Generated by Django 5.0.2 on 2024-06-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='Изображение'),
        ),
    ]