from django.contrib import admin
from news.models import Categories, Label, Post

class AdminPost(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'post_date', 'draft')
        }),
        (None, {
            'fields': ('content', )
        }),
        (None, {
            'fields': ('categories', 'label')
        }),
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    list_display = ('title', 'post_date', 'draft', 'slug')

    '''class Media:
        js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/tinymce_init.js',
        )'''

class AdminCategories(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    list_display = ('title', 'parent')

class AdminLabel(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(Categories, AdminCategories)
admin.site.register(Label, AdminLabel)
admin.site.register(Post, AdminPost)
