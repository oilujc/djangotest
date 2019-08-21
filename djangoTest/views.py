from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import (TemplateView,FormView,ListView,DetailView,View)
from django.db.models import Q

from app.models import (Book,
						Chapter,
						PageContent,
						SubChapter,
						Content)

class HomeView(TemplateView):

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		context['book'] = Book.objects.first()
		context['qs'] = self.request.GET.get('qs', None)

		if context['qs'] != None:
			try:
				context['qs'] = int(context['qs'])

				qs = Q(number=context['qs'])

				number = PageContent.objects.filter(qs)

				if number.count() <= 0:

					number = Content.objects.filter(qs)

				context['number'] = number

			except ValueError:
				pass 

			contents = PageContent.objects.filter(Q(content__contains=context['qs']) | 
													Q(chapter__title__contains=context['qs']))

			if contents.count() <= 0:

				contents = Content.objects.filter(Q(content__contains=context['qs']) | 
													Q(subchapter__title__contains=context['qs']))

			context['contents'] = contents


		return context

	def get_template_names(self):
		qs = self.request.GET.get('qs', None)
		template = 'base.html'

		if qs != None:
			template = 'search.html'

		return template

class BookView(DetailView):
	template_name= "base.html"
	slug_url_kwarg = 'slug'
	model = Book

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
			
		return context

class ChapterView(DetailView):
	template_name= "content.html"
	model = Chapter
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		try:
			context['book'] = Book.objects.get(slug=self.kwargs['book'])
		except Book.DoesNotExist:
			raise Http404
			
		return context

	def dispatch(self, *args, **kwargs):
		if self.kwargs['book']:
			return super().dispatch(*args, **kwargs)

		raise Http404


	def get_queryset(self):
		if self.kwargs['book']:
			return Chapter.objects.filter(book__slug=self.kwargs['book'])

class SubChapterView(DetailView):
	template_name= "content.html"
	model = SubChapter
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		try:
			context['book'] = Book.objects.get(slug=self.kwargs['book'])
		except Book.DoesNotExist:
			raise Http404
			
		return context

	def dispatch(self, *args, **kwargs):
		if self.kwargs['book'] and self.kwargs['chapter']:
			return super().dispatch(*args, **kwargs)

		raise Http404


	def get_queryset(self):
		if self.kwargs['book'] and self.kwargs['chapter']:
			return SubChapter.objects.filter(chapter__slug=self.kwargs['chapter'])

