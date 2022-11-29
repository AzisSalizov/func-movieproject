from django.forms import ModelForm  , TextInput
from .models import Genress

class GenressForm(ModelForm):
    class Meta:
        model = Genress
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Жанры'})
        }