from django.db import models

class Categories(models.Model):
    title = models.CharField(u"Назва", max_length=100) #Назва категорії
    slug = models.SlugField(u"Посилання")
    parent = models.ForeignKey('self') #Батьківська категорія

class Post(models.Model):
    title = models.CharField(u"Назва", max_length=250)
    categories = models.ManyToManyField(Categories)
    announce = models.TextField(u"Анонс", max_length= 250)
    content = models.TextField(u"Вміст (html)")
    slug = models.SlugField(u"Посилання")
    post_date = models.DateTimeField(u"Дата публікації")
    draft = models.BooleanField(u"Чорновик")
    meta_tags = models.TextField(u"Мета теги", max_length= 250)
