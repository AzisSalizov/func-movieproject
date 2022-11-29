from django.forms import ModelForm  , TextInput

from .models import AddFilm



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