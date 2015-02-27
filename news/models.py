# -*- coding: utf-8 -*-
from django.db import models

class Categories(models.Model):
    title = models.CharField(u"Название", max_length=100)
    slug = models.SlugField(u"Ссылка")
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.title


class Label(models.Model):
    title = models.CharField(u"Название", max_length=100)
    slug = models.SlugField(u"Ссылка")

    class Meta:
        verbose_name = 'Метку'
        verbose_name_plural = 'Метки'

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(u"Название", max_length=250)
    categories = models.ManyToManyField(Categories, blank=True, null=True)
    content = models.TextField(u"Содержимое (html)")
    slug = models.SlugField(u"Ссылка")
    post_date = models.DateTimeField(u"Дата публикации")
    draft = models.BooleanField(u"Черновик", default=False)
    label = models.ManyToManyField(Label, blank=True, null=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __unicode__(self):
        return self.title
