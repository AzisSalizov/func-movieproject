from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.HomePage , name='home' ),
    path('addfim' , views.FilmPage , name='addfilm' ),
    path('search' , views.AddFilm , name='search' ),
    path('delete-item/<int:id>' , views.Deletecard , name='delete-item' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)