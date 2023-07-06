from django.db import models

# Create your models here.
class Home(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email_id = models.CharField(max_length=255, null=True)
    mobileno = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True) 