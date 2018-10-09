# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-01 19:55
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0051_auto_20170126_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentitem',
            name='source_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='fileformat',
            name='extension',
            field=models.CharField(choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'srt', b'SRT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (
                b'png', b'PNG Image'), (b'gif', b'GIF Image'), (b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'zip', b'HTML5 Zip')], max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'vector_video', b'Vectorized'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'document_thumbnail', b'Thumbnail'), (
                b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'topic_thumbnail', b'Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_thumbnail', b'HTML5 Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
