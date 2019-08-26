from django import forms
from django.contrib import admin
from ckeditor.widgets import (CKEditorWidget,)
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (Book,
					Chapter,
					SubChapter,
					Content,
					PageContent,
					Section
					)

class SectionAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Section
		fields = '__all__'

class PageContentAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = PageContent
		fields = '__all__'

class ContentAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Content
		fields = '__all__'

# -----------------------------------------------------------------

class SectionAdmin(admin.ModelAdmin):
	form = SectionAdminForm

class BookAdmin(admin.ModelAdmin):
	search_fields = ['title','subtitle']

class ChapterAdmin(admin.ModelAdmin):
	search_fields = ['book__title','title','chapter','page_type']

class SubChapterAdmin(admin.ModelAdmin):
	search_fields = ['chapter__title','title']

class ContentAdmin(admin.ModelAdmin):
	form = ContentAdminForm
	search_fields = ['number','subchapter__title']

class PageContentAdmin(admin.ModelAdmin):
	form = PageContentAdminForm
	search_fields = ['number','chapter__title']

admin.site.register(Section, SectionAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(SubChapter, SubChapterAdmin)
admin.site.register(PageContent, PageContentAdmin)
admin.site.register(Content, ContentAdmin)

