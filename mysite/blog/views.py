from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import Http404
from .models import Post

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_posts = paginator.get_page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts': page_posts})


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post.published,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post_slug)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
