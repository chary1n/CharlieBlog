# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_article_content1'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='poll_num',
            field=models.IntegerField(default=0, verbose_name='喜欢量'),
        ),
        migrations.AddField(
            model_name='article',
            name='view_num',
            field=models.IntegerField(default=0, verbose_name='浏览量'),
        ),
    ]
