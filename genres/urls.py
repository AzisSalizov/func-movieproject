from django.urls import path
from . import views


urlpatterns = [
   path('' , views.HomePage , name='home' ),
   path('genress' , views.GenressPage , name='genress' ),
]

