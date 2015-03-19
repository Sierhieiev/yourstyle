# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fieldgroup',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settingsgroup',
            name='descriptions',
            field=models.TextField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441'),
            preserve_default=True,
        ),
    ]
