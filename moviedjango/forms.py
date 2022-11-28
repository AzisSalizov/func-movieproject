from django.forms import ModelForm  , TextInput

from .models import Genress , Category , AddFilm


class GenressForm(ModelForm):
    class Meta:
        model = Genress
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Жанры'})
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Категория'})
        }

class AddFilmForm(ModelForm):
    class Meta:
        model = AddFilm
        fields = ['title' , 'descr' , 'country' , 'genress' , 'url' , 'image']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Название'}),
            'descr': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Описание'}),
            'genress': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Жанр'}),
            'country': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Страна'}),
            'url': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Ссылка'}),
        }