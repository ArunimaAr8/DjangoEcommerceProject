from django.db import models

class CustomerData(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    mobile = models.IntegerField(unique=True)
    email = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)

#user can have multiple data in profile
class Profile(models.Model):
    username = models.ForeignKey(CustomerData,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(unique=True)
    email = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)