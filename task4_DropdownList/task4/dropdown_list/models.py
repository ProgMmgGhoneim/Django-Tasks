from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country , on_delete=models.CASCADE)
    name  =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Person(models.Model):
    name  = models.CharField(max_length=200)
    birthday =models.DateField(null=True ,blank=True)
    country = models.ForeignKey(Country ,on_delete=models.CASCADE)
    city =models.ForeignKey(City , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
