from django.shortcuts import render , redirect
from .forms import AddFilmForm 
from .models import AddFilm  
from genres.models import Genress

# Create your views here.

def HomePage(request):
    genress = Genress.objects.all()
    film = AddFilm.objects.all()
    search_query = request.GET.get('search' , '')
    if search_query:
        film = AddFilm.objects.filter(title__icontains=search_query)
    else:
        film = AddFilm.objects.all()
    context = {
      'film' : film,
      'genress':genress,
    }
    return render(request , 'moviedjango/home.html' , context)

def FilmPage(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            if request.POST.get('genress' , None):
                form.genres_id = int(request.POST.get('genress'))
            return redirect('/')
    form = AddFilmForm()
    context = {
        'form':form
    }
    return render(request , 'moviedjango/addfilm.html' ,  context)

def DeleteCard(request , pk):
    card = AddFilm.objects.filter(id=pk)
    card.delete()
    return redirect('/')


