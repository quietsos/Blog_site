from pyexpat import model
from django.db import models

class Login(models.Model):
    lusername = models.CharField(max_length=50)
    lpassword = models.CharField(max_length=50)




    def __str__(self):
        return self.lusername



class Signup(models.Model):
    sfirstname = models.CharField(max_length=50)
    slastname = models.CharField(max_length=50)
    semail = models.EmailField(max_length=50)
    sphone = models.CharField(max_length=20)


    def __str__(self):
        return self.sfirstname 

