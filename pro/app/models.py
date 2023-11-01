from django.db import models

# Create your models here.
class DataModel(models.Model):
    name=models.CharField(max_length=121)
    locality=models.CharField(max_length=121)
    mobile=models.IntegerField()
    city=models.CharField(max_length=1212)
    state= models.CharField(max_length=121)
    zipcode= models.IntegerField()