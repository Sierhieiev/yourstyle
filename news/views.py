from django.shortcuts import render, get_object_or_404
from django.views import generic
from news.models import Categories, Label, Post


class IndexView(generic.ListView):
    template_name = 'news/list.html'
    context_object_name = 'context'
    posts = Post.objects.filter(draft = False).order_by('-post_date')
    categories = Categories.objects.all()
    labels = Label.objects.all()
    queryset = {
        'posts': posts,
        'categories': categories,
        'labels': labels
    }

class CategoriesView(generic.ListView):
    template_name = 'news/list.html'
    context_object_name = 'context'

    def get_queryset(self):
        category = Categories.objects.filter(slug = self.kwargs['slug'])
        posts = Post.objects.filter(categories = category).order_by('-post_date')
        categories = Categories.objects.all()
        labels = Label.objects.all()
        queryset = {
            'posts': posts,
            'categories': categories,
            'labels': labels
        }
        return queryset

class LabelView(generic.ListView):
    template_name = 'news/list.html'
    context_object_name = 'context'

    def get_queryset(self):
        label = Label.objects.filter(slug = self.kwargs['slug'])
        posts = Post.objects.filter(label = label).order_by('-post_date')
        categories = Categories.objects.all()
        labels = Label.objects.all()
        queryset = {
            'posts': posts,
            'categories': categories,
            'labels': labels
        }
        return queryset

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



