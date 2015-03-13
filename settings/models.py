# -*- coding: utf-8 -*-
from django.db import models

#
class Settings(models.Model):
    title = models.CharField(u'Назва', max_length=100)
    system_name = models.SlugField(u'Системна назва', max_length=100, unique=True)
    descriptions = models.TextField(u'Опис', max_length=500)

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

#групування полів налаштувань в групи
class FieldGroup(Settings):
    settings_group = models.ForeignKey(SettingsGroup)
    section = models.ForeignKey(Section)
    class Meta:
        verbose_name = 'Группа полів налаштувань'
        verbose_name_plural = 'Группи полів налаштувань'

#налаштування
class Field(Settings):
    value = models.CharField(u'Значение', max_length=500)
    value_type = models.CharField(u'Тип даних', max_length=50)
    field_group = models.ForeignKey(FieldGroup)
    settings_group = models.ForeignKey(SettingsGroup)
    section = models.ForeignKey(Section)

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'