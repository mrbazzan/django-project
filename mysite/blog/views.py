from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post.published,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post_slug)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
