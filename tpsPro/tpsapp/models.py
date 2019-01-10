from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=100)
    auth=models.CharField(max_length=10)


