# Generated by Django 4.0.5 on 2022-07-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
