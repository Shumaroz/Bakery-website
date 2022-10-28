from email.policy import default
from django.conf import settings
from django.db import models

# Create your models here.


class Bulka(models.Model):
    name = models.TextField(primary_key = True)
    nachinka = models.TextField(default = "simple")
    testo = models.TextField(default = "simple")
    price = models.IntegerField(default = "0")
    text_ops = models.TextField()


    def __str__(self):
        return self.name
    
