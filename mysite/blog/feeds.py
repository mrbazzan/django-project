
from django.template.defaultfilters import truncatewords_html
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post
import markdown


class LatestPostsFeed(Feed):
    title = "My blog"
    link = reverse_lazy("blog:post_list")
    description = "Latest posts in my blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 10)

    def item_pubdate(self, item):
        return item.publish

