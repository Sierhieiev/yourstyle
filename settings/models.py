# -*- coding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from gfklookupwidget.fields import GfkLookupField


#default_type = ContentType.objects.get_by_natural_key("news", "post")

limit = {
    'model__in': ['post', 'label']
}

#
class Settings(models.Model):
    title = models.CharField(u'Назва', max_length=100)
    system_name = models.SlugField(u'Системна назва', max_length=100, unique=True)
    descriptions = models.TextField(u'Опис', max_length=500, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

#назва апа для якого будуть створены налаштування
class Section(Settings):
    class Meta:
        verbose_name = 'Секція'
        verbose_name_plural = 'Секції'

#групування налаштувань в групи
class SettingsGroup(Settings):
    section = models.ForeignKey(Section)
    class Meta:
        verbose_name = 'Группа налаштувань'
        verbose_name_plural = 'Группи налаштувань'

class ModelSettingsField(models.Model):  # Base class for db setting
    class Meta:
        abstract = True

#налаштування
class Field(Settings):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, limit_choices_to = limit)
    object_id = GfkLookupField(content_type_field_name='content_type', blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    settings_group = models.ForeignKey(SettingsGroup)
    section = models.ForeignKey(Section)

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'
