from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
									 CreateAPIView,
									 RetrieveAPIView,
									 UpdateAPIView,
									 DestroyAPIView)

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import SessionAuthentication

from app.models import (Book,
					Chapter,
					SubChapter,
					Content,
					PageContent,
					Section,

					)

from .serializers import (BookSerializer,
							SectionSerializer,
							ContentSerializer,
							PageContentSerializer,
							SubChapterSerializer,
							ChapterSerializer,
							)

from rest_framework.response import Response


class BookView(ListAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

class SectionView(ListAPIView):

	queryset = Section.objects.all()
	serializer_class = SectionSerializer
	permission_classes = [IsAuthenticated]


class ContentView(ListAPIView):

	queryset = Content.objects.all()
	serializer_class = ContentSerializer
	permission_classes = [IsAuthenticated]


class PageContentView(ListAPIView):

	queryset = PageContent.objects.all()
	serializer_class = PageContentSerializer
	permission_classes = [IsAuthenticated]


class SubChapterView(ListAPIView):

	queryset = SubChapter.objects.all()
	serializer_class = SubChapterSerializer
	permission_classes = [IsAuthenticated]


class ChapterView(ListAPIView):

	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer
	permission_classes = [IsAuthenticated]
