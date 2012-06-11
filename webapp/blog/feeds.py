from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy

from blog.models import Post

class LatestPostsFeed(Feed):
    title = "Latest posts - %s" % Site.objects.get_current().name
    link = reverse_lazy("blog.index")
    description = "The latest blog posts"

    def items(self):
        return Post.objects.listed()[:10]
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_html
