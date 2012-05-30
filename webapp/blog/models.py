from django.db import models
from django.core.urlresolvers import reverse

class PostManager(models.Manager):

    def published(self):
        return self.filter(published=True)

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
    
    published = models.BooleanField(default=False)

    objects = PostManager()

    def get_absolute_url(self):
        return reverse('blog.post', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title
