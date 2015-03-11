# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150227_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 27, 15, 37, 35, 999431), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 27, 15, 37, 35, 999480), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
