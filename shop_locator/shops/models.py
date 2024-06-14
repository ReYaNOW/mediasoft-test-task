from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class City(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=100, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}, г. {self.city.name}'


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    house = models.PositiveSmallIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def clean(self):
        if not Street.objects.filter(city=self.city).exists():
            raise ValidationError("There is not such street in this city")

        if self.opening_time >= self.closing_time:
            raise ValidationError("Opening time must be before closing time")

    def is_open(self):
        return (
            '1'
            if self.opening_time < datetime.now().time() < self.closing_time
            else '0'
        )

    def __str__(self):
        return self.name
