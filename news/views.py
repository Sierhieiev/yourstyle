# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views import generic
from news.models import Categories, Label, Post


class GenericListView(generic.ListView):
    template_name = 'news/list.html'
    context_object_name = 'posts'
    page_title = u'Останні новини'

    def get_queryset(self):
        path_info = self.request.path_info
        if path_info.find('/news/label/') != -1:
            label = get_object_or_404(Label, slug = self.kwargs['slug'])
            posts = Post.objects.filter(label = label).order_by('-post_date')
            self.page_title = label.title
        elif path_info.find('/news/category/') != -1:
            category = get_object_or_404(Categories, slug = self.kwargs['slug'])
            posts = Post.objects.filter(categories = category).order_by('-post_date')
            self.page_title = category.title
        else:
            posts = Post.objects.filter(draft = False).order_by('-post_date')
        return posts

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data(**kwargs)
        labels = Label.objects.all()
        categories = Categories.objects.all()
        context['categories'] = categories
        context['labels'] = labels
        context['page_title'] = self.page_title
        dates = Post.objects.values('post_date')
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
        return context

