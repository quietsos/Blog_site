from django.db import models

class Login(models.Model):
    lusername = models.CharField(max_length=50)
    lpassword = models.CharField(max_length=50)




    def __str__(self):
        return self.lusername


