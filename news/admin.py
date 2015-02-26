from django.contrib import admin
from news.models import Categories, Label, Post

admin.site.register(Categories)
admin.site.register(Label)
admin.site.register(Post)
