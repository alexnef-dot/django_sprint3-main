from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template = "blog/index.html"
    posts = Post.objects.filter(is_published=True,
    category__is_published=True,
    pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {"post_list": posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404("Эта категория не опубликована")
    template = "blog/category.html"
    posts = Post.objects.filter(is_published=True,
    pub_date__lte=timezone.now(), category=category)
    context = {
        "category": category,  # Добавлено для использования в шаблоне
        "post_list": posts  # или "posts": posts
    }
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.is_published:
        raise Http404("Эта пост не опубликован")
    if  not post.category.is_published:
        raise Http404("Эта категория не опубликована")
    if post.pub_date > timezone.now():
        raise Http404("Эта пост не опубликован по времени")
    context = {"post": post}
    template = "blog/detail.html"
    return render(request, template, context)
