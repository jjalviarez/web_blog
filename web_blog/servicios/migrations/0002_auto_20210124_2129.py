# Generated by Django 3.0.11 on 2021-01-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='image',
            field=models.ImageField(upload_to='servicio'),
        ),
    ]
