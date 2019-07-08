from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from utils.generators import unique_slug_generator, unique_slug_chapter_generator
# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100,blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)
	author = models.CharField(max_length=100)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"

	def __str__(self):
		return self.title

class Chapter(models.Model):

	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	chapter = models.IntegerField()
	slug = models.SlugField(blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)

	page_type = models.CharField(max_length=2, choices=(('pa', 'page'), ('ch', 'chapter')), default='ch')

	class Meta:
		verbose_name = "Chapter"
		verbose_name_plural = "Chapters"

	def __str__(self):
		return self.title

class PageContent(models.Model):

	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	content = RichTextField()

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "PageContent"
		verbose_name_plural = "PageContents"

	def __str__(self):
		return "{}) {}".format(self.pk, self.chapter.title)

class SubChapter(models.Model):

	chapter = models.ForeignKey(Chapter, on_delete= models.CASCADE)
	title = models.CharField(max_length=150)
	slug = models.SlugField(blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "SubChapter"
		verbose_name_plural = "SubChapters"

	def __str__(self):
		return self.title

class Content(models.Model):

	subchapter = models.ForeignKey(SubChapter, on_delete=models.CASCADE)
	content = RichTextField()

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Content"
		verbose_name_plural = "Contents"

	def __str__(self):
		return "{}) {}".format(self.pk, self.subchapter.title)

@receiver(post_save, sender=Book)
def post_save_book(sender, instance,created, **kwargs):
	instance.title = instance.title.lower()
	if not instance.slug:
		instance.slug = "{0}".format(unique_slug_generator(instance))
		instance.save()

@receiver(post_save, sender=Chapter)
def post_save_chapter(sender, instance,created, **kwargs):
	instance.title = instance.title.lower()
	if not instance.slug:
		instance.slug = "{0}".format(unique_slug_generator(instance, "chapter-{}".format(instance.chapter)))
		instance.save()

@receiver(post_save, sender=SubChapter)
def post_save_sub_chapter(sender, instance,created, **kwargs):
	instance.title = instance.title.lower()
	if not instance.slug:
		instance.slug = "{0}".format(unique_slug_generator(instance, "subchapter-{}".format(instance.pk)))
		instance.save()