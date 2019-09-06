"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, BookView, ChapterView, SubChapterView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home"),

    path('book/<slug:slug>/', BookView.as_view(), name="book"),
    path('book/<slug:book>/<slug:slug>/', ChapterView.as_view(), name="chapter"),
    path('book/<slug:book>/<slug:chapter>/<slug:slug>', SubChapterView.as_view(), name="subchapter"),

    #Api
    path('api/', include('api.urls', namespace='api')),

    #Third apps
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    #static = Funcion auxiliar para devolver un patron de URL para servir archivos en modo debug
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)