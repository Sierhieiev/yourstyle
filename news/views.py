# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.template import defaultfilters
from django.views import generic
from news.models import Categories, Label, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class GenericListView(generic.ListView):
    template_name = 'news/list.html'
    context_object_name = 'posts'
    page_title = u'Останні новини'

    def get_queryset(self):
        path_info = self.request.path_info

        if path_info.find('/news/label/') != -1:
            label = get_object_or_404(Label, slug = self.kwargs['slug'])
            posts_list = Post.objects.filter(label = label, draft = False).order_by('-post_date')
            self.page_title = label.title.capitalize()
        elif path_info.find('/news/category/') != -1:
            category = get_object_or_404(Categories, slug = self.kwargs['slug'])
            posts_list = Post.objects.filter(categories = category, draft = False).order_by('-post_date')
            self.page_title = category.title
        else:
            posts_list = Post.objects.filter(draft = False).order_by('-post_date')

        page = self.request.GET.get('page')
        posts = create_paginator(posts_list, page)
        return posts

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data(**kwargs)
        labels = Label.objects.all()
        categories = Categories.objects.all()
        context['categories'] = categories
        context['labels'] = labels
        context['page_title'] = self.page_title
        dates = Post.objects.datetimes('post_date', 'month')
        context['dates'] = dates
        return context


class PostView(generic.DetailView):
    template_name = 'news/post.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        labels = Label.objects.all()
        categories = Categories.objects.all()
        context['categories'] = categories
        context['labels'] = labels
        dates = Post.objects.datetimes('post_date', 'month')
        context['dates'] = dates
        return context

class ArchiveView(generic.MonthArchiveView):
    model = Post
    template_name = 'news/list.html'
    context_object_name = 'posts'
    date_field="post_date"
    month_format='%m'

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        labels = Label.objects.all()
        categories = Categories.objects.all()
        context['categories'] = categories
        context['labels'] = labels
        dates = Post.objects.datetimes('post_date', 'month')
        context['dates'] = dates
        month = self.kwargs['month']
        year = self.kwargs['year']
        current_month_archive = datetime.date(int(year), int(month), 1)
        context['page_title'] = defaultfilters.date(current_month_archive, 'F Y')

        posts_list = kwargs['object_list']
        page = self.request.GET.get('page')
        context['posts'] = create_paginator(posts_list, page)
        return context

def create_paginator(posts_list, page):
    paginator = Paginator(posts_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return posts
