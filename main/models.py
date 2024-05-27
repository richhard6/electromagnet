from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Tender(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    closing_date = models.DateField()
    company = models.CharField(max_length=100)

class Curriculum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.TextField()
    education = models.TextField()

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shares = models.IntegerField()
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)