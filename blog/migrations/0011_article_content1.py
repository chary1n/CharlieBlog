# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 09:05
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170526_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content1',
            field=markdownx.models.MarkdownxField(default=1),
            preserve_default=False,
        ),
    ]