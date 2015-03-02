from django.shortcuts import render, get_object_or_404
from django.views import generic
from news.models import Categories, Label, Post


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'context'
    posts = Post.objects.filter(draft = False).order_by('-post_date')
    categories = Categories.objects.all()
    queryset = {
        'posts': posts,
        'categories': categories
    }

def post(request, slug):
    news = get_object_or_404(Post, slug = slug)
    return render(request, 'news/post.html', {'news': news})

def category(request, slug):
    categories = get_object_or_404(Categories, slug = slug)
    return render(request, 'news/post.html', {'categories': categories})
