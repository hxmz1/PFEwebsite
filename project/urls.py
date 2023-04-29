
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singup', include('compte.urls')),
    path('', include('home.urls')),
    path('connexion', include('connexion.urls')),
    #path('map/', include('compte.urls')),
    #path('', include('superviseur.urls')),
    #path('', include('client.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    