# Generated by Django 3.0.11 on 2021-01-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='post', to='blog.Category'),
        ),
    ]
