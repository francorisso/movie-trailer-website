# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20150302_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_image_ext',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 17, 8, 36, 976312), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_image_url',
            field=models.ImageField(upload_to=b'images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 17, 8, 36, 976347), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
