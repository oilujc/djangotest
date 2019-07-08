# Generated by Django 2.2.3 on 2019-07-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_chapter_content_subchapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
