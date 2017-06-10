# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
import uuid

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from markdownx.models import MarkdownxField


class Category(models.Model):
    def _category_url(self):
        return reverse('blog:article_list_by_category', args=[self.id])

    @property
    def article_count(self):
        return len(Article.objects.filter(category_id=self.id))

    name = models.CharField(max_length=100)
    url = property(_category_url)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Article(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=101)
    tag = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField("Publish Date", auto_now_add = True)  #博客日期
    create_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank=True, null=True)  #博客文章正文
    content1 = MarkdownxField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    view_num = models.IntegerField(u"浏览量",default=0)
    poll_num = models.IntegerField(u"喜欢量",default=0)

    def add_view_num(self):
        self.view_num += 1

    def add_poll_num(self):
        self.poll_num += 1

    # create_time.editable = True
    # date_time.editable = True
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
