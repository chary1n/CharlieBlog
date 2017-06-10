# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from blog.models import Article, Category


def index(request):
    ret = Category.objects.get_queryset()
    # for cate in ret:
        # cate.count = Article.objects.filter({'category_id': cate.id})
    return  render(request, 'blog/index.html', {
        'category': ret,
    })

def detail(request):
    return render(request, 'blog/detail.html')


def category(request):
    ret = Category.objects.get_queryset()
    json_got = serializers.serialize('json', ret)
    json_obj = json.loads(json_got)
    for obj in json_obj:
        obj['fields']['url'] = reverse('blog:article_list_by_category', args=[obj['pk']])
    return JsonResponse(json_obj, safe=False)


def article_list_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = category.article_set.all()

    return render(request, 'blog/detail.html', {
        'articles':articles,
    })