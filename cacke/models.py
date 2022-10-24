from django.conf import settings
from django.db import models

# Create your models here.


class Bulka(models.Model):
    name = models.TextField(primary_key = True)
    nachinka = models.TextField()
    text_ops = models.TextField()


    def __str__(self):
        return self.name
    
