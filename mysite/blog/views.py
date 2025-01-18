from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count
from .models import Post, Comment
from django.http import Http404
from taggit.models import Tag

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_posts = paginator.get_page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts': page_posts, 'tag': tag})


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post.published,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post_slug)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    post_tag_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids) \
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                                 .order_by('-same_tags', '-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post, 'comments': comments, 'form': form,
                   'similar_posts': similar_posts})


def post_share(request, post_id):
    sent = False
    post = get_object_or_404(Post.published, id=post_id)
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{form_data['name']} recommends you read "\
                      f"<em>{post.title}</em>"
            message = f"Read <em>{post.title}</em> at\n\t{post_url}\n\n"\
                      f"{form_data['name']}'s comment: {form_data['comment']}"
            send_mail(subject, message, '', [form_data['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'form': form, 'post': post, 'sent': sent})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post.published, id=post_id)
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request,
                  'blog/post/comment.html',
                  {'post': post, 'form': form, 'comment': comment})
