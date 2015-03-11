# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20150227_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='api_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.MovieGenres'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='revenue',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 14, 17, 8, 181509), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 14, 17, 8, 181552), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
