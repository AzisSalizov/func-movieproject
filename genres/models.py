from django.db import models

# Create your models here.

class Genress(models.Model):
    title = models.CharField('Жанры' , max_length=255)

    def __str__(self):
      return self.title