from django.db import models

class Registerdata(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=35)
    dep=models.CharField(max_length=20)
    gender=models.CharField(max_length=12)
            
