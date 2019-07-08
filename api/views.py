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
					Content
					)

from .serializers import (BookSerializer
							)

from rest_framework.response import Response


class BookView(ListAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

# class BookView(ListAPIView):

# 	queryset = Book.objects.all()
# 	serializer_class = BookSerializer
# 	permission_classes = [IsAuthenticated]
