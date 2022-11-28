from django.shortcuts import render , redirect
from .forms import AddFilmForm , GenressForm , CategoryForm
from .models import AddFilm , Genress , Category

# Create your views here.

def HomePage(request):
    genress = Genress.objects.all()
    film = AddFilm.objects.all()
    category = Category.objects.all()
    search_query = request.GET.get('search' , '')
    if search_query:
        film = AddFilm.objects.filter(title__icontains=search_query)
    else:
        film = AddFilm.objects.all()
    context = {
      'film' : film,
      'genress':genress,
      'category':category
    }
    return render(request , 'moviedjango/home.html' , context)

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

def GenressPage(request):
    if request.method == 'POST':
        form = GenressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = GenressForm()
    return render(request , 'moviedjango/genress.html' , {'form':form})

def CategoryPage(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = CategoryForm()
    return render(request , 'moviedjango/category.html' , {'form' : form})
