import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTest.settings")
django.setup()

from app.models import Chapter, SubChapter

chapters = Chapter.objects.all()
subchapters = SubChapter.objects.all()

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


# for chapter in chapters:
# 	for word in word_list:
# 		if word.lower() in chapter.title:
# 			chapter.title = chapter.title.replace(word.lower(),word)

# 	chapter.save()

for subchapter in subchapters:
	for word in word_sc_list:
		if word.lower() in subchapter.title:
			print(word)
			subchapter.title = subchapter.title.replace(word.lower(),word)

	subchapter.save()
