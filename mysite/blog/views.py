from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post.published, id=id)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
