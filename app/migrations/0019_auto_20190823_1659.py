# Generated by Django 2.2.4 on 2019-08-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190823_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subchapter',
            options={'ordering': ['pk'], 'verbose_name': 'SubChapter', 'verbose_name_plural': 'SubChapters'},
        ),
        migrations.AddField(
            model_name='content',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
