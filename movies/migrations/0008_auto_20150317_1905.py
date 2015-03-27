# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20150302_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 19, 5, 36, 164914), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_image_url',
            field=models.ImageField(upload_to=b'movies__posters', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 19, 5, 36, 164944), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
