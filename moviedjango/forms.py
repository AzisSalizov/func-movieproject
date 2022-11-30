from django.forms import ModelForm  , TextInput ,Select

from .models import AddFilm



class AddFilmForm(ModelForm):
    class Meta:
        model = AddFilm
        fields = ['title' , 'descr' , 'country' , 'genress' , 'url' , 'image']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Название'}),
            'descr': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Описание'}),
            'genress': Select(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Жанр' ,'name': 'genres'}),
            'country': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Страна'}),
            'url': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Ссылка'}),
        }