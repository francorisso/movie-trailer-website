# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150216_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 18, 6, 45, 121932), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 18, 6, 45, 121967), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
