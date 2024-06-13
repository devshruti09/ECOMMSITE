from django.db import models

# Create your models here.
class Bakery(models.Model):
    name=models.TextField(max_length=50)
    email=models.EmailField
    phone=models.IntegerField
    message=models.TextField(max_length=150)


