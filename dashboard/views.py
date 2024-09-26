from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .models import Setting, Comment, Category, Post


def index(request):
    config = Setting.objects.filter(id=1).first()
    
    categories = Category.objects.values()
    
    data_post = Post.objects.order_by('-created_at')
    
    paginator = Paginator(data_post, 20)
    
    page_paginate = request.GET.get('page', 1)
    
    posts = paginator.get_page(page_paginate) # showing every page only 20 posts
    
    context = {
        'setting': config,
        'categories': categories,
        'posts': posts,
        'paginate': paginator
    }
    
    return render(request, 'home.html', context)
    
    
def post(request, slug):
    
    config = Setting.objects.filter(id=1).first()
    
    categories = Category.objects.values()
    
    post = Post.objects.filter(slug=slug).first()
    
    comments = Comment.objects.filter(post_id=post.id).order_by("-created_at")[:20]
    
    recommneded_post = Post.objects.filter(category=post.category).exclude(slug=slug).order_by("-created_at")[:5]
    
    context = {
        'setting': config,
        'categories': categories,
        'post': post,
        'comments': comments,
        'recommned_posts': recommneded_post
    }
    
    return render(request, 'post.html', context)


def category(request, slug):
    
    cat = Category.objects.filter(slug=slug).first()
    
    config = Setting.objects.filter(id=1).first()
    
    categories = Category.objects.values()
    
    data_posts = Post.objects.filter(category=cat).order_by("-created_at")
    
    page_number = request.GET.get('page', 1)
    
    Paginate = Paginator(data_posts, 20)
    
    posts = Paginate.get_page(page_number)
    
    context = {
        
        'setting': config,
        'categories': categories,
        'posts': posts,
    }
    
    return render(request, "category.html", context)


def search(request):
    
    config = Setting.objects.filter(id=1).first()
    
    categories = Category.objects.values()
    
    query = request.GET.get('q')
    
    if query:
        posts = Post.objects.filter(name_icontains=query) | Post.objects.filter(detail_icontains=query)
    else:
        posts = Post.objects.none()
    
    count = posts.count()
    
    context = {
        'setting': config,
        'categories': categories,
        'posts': posts,
        'count': count
    }
    
    return render(request, "search.html", context)
    
        
    
    

def notfound(request):
    render(request, '404.html', status=404)