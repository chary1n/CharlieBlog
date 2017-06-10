# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget

from blog.models import Article, Category

admin.site.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'content']}),
                 ('Tags', {'fields': ['tag', 'category_id']})]

    list_display = ['title', 'category_id', 'date_time']

    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
        MarkdownxField: {'widget': AdminMarkdownxWidget}
    }

admin.site.register(Article, ArticleAdmin)
