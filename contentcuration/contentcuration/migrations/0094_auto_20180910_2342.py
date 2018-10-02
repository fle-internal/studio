# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 23:42
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0093_auto_20180831_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileformat',
            name='extension',
            field=models.CharField(choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (b'png', b'PNG Image'), (b'gif', b'GIF Image'), (
                b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'graphie', b'Graphie Exercise'), (b'zip', b'HTML5 Zip'), (b'epub', b'ePub Document')], max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'vector_video', b'Vectorized'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'video_dependency', b'Video (dependency)'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'epub', b'ePub Document'), (b'document_thumbnail', b'Thumbnail'), (
                b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'topic_thumbnail', b'Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_dependency', b'HTML5 Dependency (Zip format)'), (b'html5_thumbnail', b'HTML5 Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
