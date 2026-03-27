# -*- coding: utf-8-*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render

from .models import Post, Category

# Create your views here.
def home(request):
    post = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    context = {
        'post': post
    }
    return render(request, 'blog/home.html', context)

def datail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.ACTIVE)

    context ={
        'post':post,
    }
    return render(request, 'blog/detail.html', context)
