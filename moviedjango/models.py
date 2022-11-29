from django.db import models

# Create your models here.
    
class AddFilm(models.Model):
    title = models.CharField('Название' , max_length=255)
    descr = models.CharField('Описание' , max_length=255)
    country = models.CharField('Страна' , max_length=255)
    genress = models.CharField('Жанр' , max_length=255)
    url = models.CharField('Ссылка' , max_length=255)
    image = models.ImageField(upload_to='images')

    
    def __str__(self):
      return self.title
    
   