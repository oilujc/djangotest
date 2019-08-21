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

class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm

class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm

class PageContentAdmin(admin.ModelAdmin):
    form = PageContentAdminForm

admin.site.register(Section, SectionAdmin)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(SubChapter)
admin.site.register(PageContent, PageContentAdmin)

admin.site.register(Content, ContentAdmin)
