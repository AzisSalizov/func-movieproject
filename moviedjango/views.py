from django.shortcuts import render , redirect
from .forms import AddFilmForm 
from .models import AddFilm 

# Create your views here.



def FilmPage(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = AddFilmForm()
    context = {
        'form':form
    }
    return render(request , 'moviedjango/addfilm.html' ,  context)


