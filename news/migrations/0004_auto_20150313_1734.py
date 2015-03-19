# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150310_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044e', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': '\u041c\u0456\u0442\u043a\u0443', 'verbose_name_plural': '\u041c\u0456\u0442\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u0417\u0430\u043f\u0438\u0441', 'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(verbose_name=b'\xd0\x91\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd1\x96\xd0\xb2\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f', blank=True, to='news.Categories', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='news.Categories', null=True, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='\u0427\u043e\u0440\u043d\u043e\u0432\u0438\u043a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.ManyToManyField(to='news.Label', null=True, verbose_name='\u041c\u0456\u0442\u043a\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 15, 34, 54, 580000, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
            preserve_default=True,
        ),
    ]
