from django.shortcuts import render ,  redirect
from .forms import GenressForm
from .models import Genress
from moviedjango.models import AddFilm 

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

def GenressPage(request):
    if request.method == 'POST':
        form = GenressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = GenressForm()
    return render(request , 'moviedjango/genress.html' , {'form':form})