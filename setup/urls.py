from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Adicione o admin do Django para gerenciar os modelos
    path('admin/', admin.site.urls), 
    
    # Inclui todas as URLs do seu app 'projeto_webII_app'
    path('', include('projeto_webII_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)