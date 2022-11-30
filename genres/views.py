from django.shortcuts import render ,  redirect
from .forms import GenressForm
# Create your views here.



def GenressPage(request):
    if request.method == 'POST':
        form = GenressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = GenressForm()
    return render(request , 'genres/genress.html' , {'form':form})