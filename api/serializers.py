from rest_framework import serializers

from app.models import (Book,
					Chapter,
					SubChapter,
					Content,
					PageContent,
					Section
					)


class SectionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Section
		fields = (
				'id',
				'title',
				'slug',
				'content'
		 		)

		read_only_fields = (
				'id',
				'title',
				'slug',
				'content',
		 		)

class ContentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Content
		fields = (
				'id',
				'content',
				'number'
		 		)

		read_only_fields = (
				'id',
				'content',
		 		)

class PageContentSerializer(serializers.ModelSerializer):

	class Meta:
		model = PageContent
		fields = (
				'id',
				'content',
				'number'
		 		)

		read_only_fields = (
				'id',
				'content',
				'number'
		 		)


class SubChapterSerializer(serializers.ModelSerializer):

	content = serializers.SerializerMethodField()

	class Meta:
		model = SubChapter
		fields = (
				'id',
				'title',
				'slug',
				'content',
		 		)

		read_only_fields = (
				'id',
				'title',
				'slug',
				'content',
		 		)

	def get_content(self, obj):
		return ContentSerializer(obj.content_set.all().order_by('pk'),many=True).data

class ChapterSerializer(serializers.ModelSerializer):

	subchapter = serializers.SerializerMethodField()
	page_content = serializers.SerializerMethodField()
	
	def get_page_content(self, obj):
		return PageContentSerializer(obj.pagecontent_set.all(),many=True).data

	def get_subchapter(self, obj):
		return SubChapterSerializer(obj.subchapter_set.all().order_by('pk'),many=True).data

	class Meta:
		model = Chapter
		fields = (
				'id',
				'title',
				'slug',
				'chapter',
				'subchapter',
				'page_type',
				'page_content'
		 		)

		read_only_fields = (
				'id',
				'title',
				'slug',
				'chapter',
				'subchapter',
				'page_type',
				'page_content'
		 		)


class BookSerializer(serializers.ModelSerializer):
	
	chapter = serializers.SerializerMethodField()  

	class Meta:
		model = Book
		fields = (
				'id',
				'title',
				'subtitle',
				'slug',
				'chapter',
		 		)

		read_only_fields = (
				'id',
				'subtitle',
				'title',
				'slug',
				'chapter',
		 		)

	def get_chapter(self, obj):
		return ChapterSerializer(obj.chapter_set.all().order_by('-page_type'),many=True).data


