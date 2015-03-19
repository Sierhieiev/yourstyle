# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20150316_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldgroup',
            name='section',
        ),
        migrations.RemoveField(
            model_name='fieldgroup',
            name='settings_group',
        ),
        migrations.RemoveField(
            model_name='field',
            name='field_group',
        ),
        migrations.DeleteModel(
            name='FieldGroup',
        ),
        migrations.AlterField(
            model_name='field',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='value',
            field=models.TextField(max_length=100, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingsgroup',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441', blank=True),
            preserve_default=True,
        ),
    ]
