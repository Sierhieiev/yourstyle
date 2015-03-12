# -*- coding: utf-8 -*-
from django.db import models

#назва апа для якого будуть створены налаштування
class Appllications(models.Model):
    title = models.CharField(u'Назва', max_length=250)

#групування налаштувань в групи
class GroupSettings(models.Model):
    title = models.CharField(u'Назва', max_length=250)

#групування полів налаштувань в групи
class FieldGroup(models.Model):
    title = models.CharField(u'Назва', max_length=250)

#налаштування
class Field(models.Model):
    title = models.CharField(u'Назва', max_length=250)