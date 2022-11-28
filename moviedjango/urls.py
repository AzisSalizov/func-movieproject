from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.HomePage , name='home' ),
    path('addfim' , views.FilmPage , name='addfilm' ),
    path('genress' , views.GenressPage , name='genress' ),
    path('category' , views.CategoryPage , name='category' ),
    path('search' , views.AddFilm , name='search' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)