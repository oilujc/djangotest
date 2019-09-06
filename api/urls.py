from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import (BookView,SectionView)

app_name = 'api'
urlpatterns = [

    path('books/', BookView.as_view(), name='books_list'),
    path('sections/', SectionView.as_view(), name='section_list'),

]
