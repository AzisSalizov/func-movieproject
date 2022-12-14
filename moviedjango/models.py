from django.db import models
from genres.models import Genress

# Create your models here.
    
class AddFilm(models.Model):
    title = models.CharField('Название' , max_length=255)
    descr = models.CharField('Описание' , max_length=255)
    country = models.CharField('Страна' , max_length=255)
    genress = models.ForeignKey(Genress , on_delete=models.CASCADE)
    url = models.CharField('Ссылка' , max_length=255)
    image = models.ImageField(upload_to='images')

    
    def __str__(self):
      return self.title
    
   