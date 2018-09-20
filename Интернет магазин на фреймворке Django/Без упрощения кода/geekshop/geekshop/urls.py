from django.contrib import admin
from django.urls import re_path, include
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    re_path(r'^contact/$', mainapp.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
