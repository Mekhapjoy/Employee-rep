from django.db import models

# Create your models here.
class employee(models.Model):
    username=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)
    image=models.ImageField(null=True)
    designation=models.CharField(max_length=20,null=True)


