# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

class Categories(models.Model):
    title = models.CharField(u"Назва", max_length=100)
    slug = models.SlugField(u"Посилання", unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name = 'Батьківська категорія')

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:category', kwargs={'slug' : self.slug})


class Label(models.Model):
    title = models.CharField(u"Назва", max_length=100)
    slug = models.SlugField(u"Посилання", unique=True)

    class Meta:
        verbose_name = 'Мітку'
        verbose_name_plural = 'Мітки'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:label', kwargs={'slug' : self.slug})


class Post(models.Model):
    title = models.CharField(u"Назва", max_length=250)
    categories = models.ManyToManyField(Categories, blank=True, null=True, verbose_name = u'Категорії')
#    content = models.TextField(u"Содержимое (html)")
    content = RichTextField(u"Контент", config_name='default_config')
    slug = models.SlugField(u"Посилання", unique=True)
    post_date = models.DateTimeField(u"Дата публікації", default = timezone.now())
    draft = models.BooleanField(u"Чорновик", default=False)
    label = models.ManyToManyField(Label, blank=True, null=True, verbose_name = u'Мітки')

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post', kwargs={'slug' : self.slug})

    def get_preview(self):
        post_text = self.content
        arr = post_text.split('<!--more-->')
        return arr[0]

    def get_categories_list(self):
        return u" %s" % (u", ".join([category.title for category in self.categories.all()]))
    get_categories_list.short_description = u'Категорії'

    def get_labels_list(self):
        return u" %s" % (u", ".join([label.title for label in self.label.all()]))
    get_labels_list.short_description = u'Мітки'
