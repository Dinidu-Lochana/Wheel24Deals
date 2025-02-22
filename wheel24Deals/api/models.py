from django.db import models
from django.core.validators import MinValueValidator

class Vehicle(models.Model):
    vehicleName = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    noPlate = models.CharField(max_length=10)
    manufactureYear = models.IntegerField(validators=[MinValueValidator(1900)])
    registeredYear = models.IntegerField(validators=[MinValueValidator(1900)])
    mileage = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicleName
