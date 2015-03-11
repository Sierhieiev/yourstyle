# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('slug', models.SlugField(verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f')),
                ('parent', models.ForeignKey(to='news.Categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('slug', models.SlugField(verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('announce', models.TextField(max_length=250, verbose_name='\u0410\u043d\u043e\u043d\u0441')),
                ('content', models.TextField(verbose_name='\u0412\u043c\u0456\u0441\u0442 (html)')),
                ('slug', models.SlugField(verbose_name='\u041f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f')),
                ('post_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457')),
                ('draft', models.BooleanField(verbose_name='\u0427\u043e\u0440\u043d\u043e\u0432\u0438\u043a')),
                ('meta_tags', models.TextField(max_length=250, verbose_name='\u041c\u0435\u0442\u0430 \u0442\u0435\u0433\u0438')),
                ('categories', models.ManyToManyField(to='news.Categories')),
                ('label', models.ManyToManyField(to='news.Label')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
