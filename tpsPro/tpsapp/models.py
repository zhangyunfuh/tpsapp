from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=100)
    auth=models.CharField(max_length=10)


class wheel(models.Model):
    img=models.CharField(max_length=200)
    trackid=models.CharField(max_length=30)
    class Meta:
        db_table='wheel'

