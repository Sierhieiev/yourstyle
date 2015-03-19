# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20150313_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='system_name',
            field=models.SlugField(unique=True, max_length=100, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fieldgroup',
            name='system_name',
            field=models.SlugField(unique=True, max_length=100, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fieldgroup',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='system_name',
            field=models.SlugField(unique=True, max_length=100, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingsgroup',
            name='system_name',
            field=models.SlugField(unique=True, max_length=100, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingsgroup',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
    ]
