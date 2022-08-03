from django.db import models

# Create your models here.

class MySkill(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=500, blank=False)
    datetime = models.DateTimeField()



    def summary(self):
        return self.desc[0:100]

    def __str__(self):
        return self.title


class Contactinfo(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField(max_length=50)
    cquery = models.TextField(max_length=1000)

    

    def __str__(self):
        return self.cname
        
