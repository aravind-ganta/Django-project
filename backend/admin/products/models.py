from django.db import models

# Create your models here.
class Products(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField(max_length=1000)
    image=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)