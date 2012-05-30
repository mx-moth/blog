from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

    fieldsets = [
        (None, {
            'fields': [
                'title',
                'slug',
                'body_html'
            ]
        }),
    ]

admin.site.register(Post, PostAdmin)
