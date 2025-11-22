from django.contrib import admin
from django.urls import path, include
from Metaphyta import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('usuarios.urls')),

    path('', include('main_pages.urls')),

    path('', include('analises.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)