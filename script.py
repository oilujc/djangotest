import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTest.settings")
django.setup()

from app.models import Book, Chapter, SubChapter


chapters = Chapter.objects.all()
subchapters = SubChapter.objects.all()
books = Book.objects.all()

word_list = ["Trinidad",
			"Santísima",
			"Biblia",
			"Tradición",
			"Papa",
			"Iglesia",
			"Sacramentos",
			"María",
			"Santos",
			"Virgen",
			"Cristo"]

word_sc_list = ["Trinidad",
			"Santísima",
			"Biblia",
			"Tradición",
			"Hospitalito de la Fe",
			"Hospitalitos de la Fe",
			"Católica",
			"Pedro",
			"Eucaristía",
			"Confesión",
			"Confirmación",
			"Enfermos",
			"Unción",
			"Matrimonio",
			"Madre",
			"Rosario",
			"Reina",
			"Dios",
			"Papa",
			"Sacramento",
			"Sacerdocio",
			"Iglesia",
			"Cristo",
			"Jesucristo",
			"Sacramentos",
			"María",
			"Santos",
			"jehová",
			"Virgen"]

number = 8
for book in books:
	print(book.title)
	for chapter in book.chapter_set.filter(page_type="ch"):
		print("Capítulo {}) {}".format(chapter.chapter,chapter.title))
		for subchapter in chapter.subchapter_set.all():
			print(subchapter.title)

			for content in subchapter.content_set.all().order_by("number").order_by("pk").order_by('position'):
				content.number = number
				print(content.number)
				content.save()
				number += 1

for chapter in chapters:
	for word in word_list:
		if word.lower() in chapter.title:
			chapter.title = chapter.title.replace(word.lower(),word)

	chapter.save()

for subchapter in subchapters:
	for word in word_sc_list:
		if word.lower() in subchapter.title:
			print(word)
			subchapter.title = subchapter.title.replace(word.lower(),word)

	subchapter.save()
