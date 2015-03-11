# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': '\u041c\u0435\u0442\u043a\u0443', 'verbose_name_plural': '\u041c\u0435\u0442\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='announce',
        ),
        migrations.RemoveField(
            model_name='post',
            name='meta_tags',
        ),
        migrations.AlterField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(blank=True, to='news.Categories', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='slug',
            field=models.SlugField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='news.Categories', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 (html)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='\u0427\u0435\u0440\u043d\u043e\u0432\u0438\u043a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.ManyToManyField(to='news.Label', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
