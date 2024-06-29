"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Proyecto1.views import dia_de_hoy, saludo_nombre
from django.conf.urls.static import static

# endpoints...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', include('ecommerce.urls')), #ruteo
    path('fecha/', dia_de_hoy),
    path('saludar/<name>', saludo_nombre),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)