from django.urls import path
from . import views


urlpatterns = [
   path('genres' , views.GenressPage , name='genress' ),
]

