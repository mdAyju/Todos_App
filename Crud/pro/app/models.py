from django.db import models

# Create your models here.
class MobileModel(models.Model):
    mobiles=models.CharField(max_length=121)
    price=models.CharField(max_length=121)
    ram=models.CharField(max_length=121)
    storage=models.CharField(max_length=121)

    def __str__(self):
        return self.mobiles