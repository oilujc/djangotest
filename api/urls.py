from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import (BookView,
					SectionView,
					ContentView,
					PageContentView,
					SubChapterView,
					ChapterView,
					)

app_name = 'api'
urlpatterns = [

    path('books/', BookView.as_view(), name='books_list'),
    path('sections/', SectionView.as_view(), name='section_list'),
    path('content/', ContentView.as_view(), name='content_list'),
    path('page-content/', PageContentView.as_view(), name='page_content_list'),
    path('sub-chapter/', SubChapterView.as_view(), name='sub_chapter_list'),
    path('chapter/', ChapterView.as_view(), name='chapter_list'),

]
