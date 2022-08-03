from django.db import models

# Create your models here.

class MySkill(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=500, blank=False)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title

