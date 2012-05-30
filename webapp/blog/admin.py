from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published']

    prepopulated_fields = {'slug': ['title']}

    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                'body_html'
            ]
        }),
        ('Meta', {
            'fields': ['published'],
        })
    ]

admin.site.register(Post, PostAdmin)
