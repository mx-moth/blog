from django.db import models
from django.db.models.query import QuerySet
from django.core.urlresolvers import reverse

class PostFilterMixin(object):
    """
    A mixin that can be applied to both `Manager`s and `QuerySet`s, to filter
    posts.
    """
    def public(self):
        """
        Get all the public posts
        """
        return self.filter(public=True)
    def published(self):
        """
        Get all the published posts
        """
        return self.filter(published=True)
    def listed(self):
        """
        Get all posts that should be displayed in public listings.
        This is all the posts that are both public and published.
        """
        return self.public().published()

class PostManager(models.Manager, PostFilterMixin):
    class PostQuerySet(QuerySet, PostFilterMixin):
        pass

    def get_query_set(self):
        return PostManager.PostQuerySet(self.model)

class Post(models.Model):

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']

    title = models.CharField(max_length=255)
    body_html = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=255)
    
    published = models.BooleanField(
        default=False,
        help_text='Is this post accessible on the front end?',
    )
    public = models.BooleanField(
        default=True,
        help_text='Is this post listed in post listings like the index, archive and RSS feed?',
    )

    objects = PostManager()

    def get_absolute_url(self):
        return reverse('blog.post', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title
