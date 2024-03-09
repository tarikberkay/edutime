from django.db import models



class Register(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=True)
    password2 = models.CharField(max_length=200, null=True)

