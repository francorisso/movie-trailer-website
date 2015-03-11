# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('story_line', models.TextField(max_length=1000)),
                ('description', models.TextField()),
                ('poster_image_url', models.CharField(max_length=200)),
                ('trailer_youtube_url', models.CharField(max_length=200)),
                ('released_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
