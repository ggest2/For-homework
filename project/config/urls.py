from django.contrib import admin
from django.urls import path, include
from mzfinder import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('mzfinder/', include('mzfinder.urls')), 
    path('common/', include('common.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)