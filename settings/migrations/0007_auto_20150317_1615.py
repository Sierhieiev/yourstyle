# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('settings', '0006_auto_20150316_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='value',
        ),
        migrations.RemoveField(
            model_name='field',
            name='value_type',
        ),
        migrations.AddField(
            model_name='field',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
