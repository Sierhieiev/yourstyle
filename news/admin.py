from django.contrib import admin
from news.models import Categories, Label, Post

class AdminPost(admin.ModelAdmin):
    class Media:
        js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/tinymce_init.js',
        )

admin.site.register(Categories)
admin.site.register(Label)
admin.site.register(Post, AdminPost)
