# Generated by Django 4.2.19 on 2025-02-17 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleName', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('noPlate', models.CharField(max_length=10)),
                ('manufactureYear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)])),
                ('registeredYear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)])),
                ('mileage', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
