from django import forms
from django.contrib import admin
from ckeditor.widgets import (CKEditorWidget,)

from .models import (Book,
					Chapter,
					SubChapter,
					Content,
					PageContent
					)

class ContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Content
        fields = '__all__'

class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(PageContent, ContentAdmin)
admin.site.register(SubChapter)
admin.site.register(Content, ContentAdmin)
