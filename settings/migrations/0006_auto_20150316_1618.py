# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20150316_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='value_type',
            field=models.CharField(max_length=50, verbose_name='\u0422\u0438\u043f \u0434\u0430\u043d\u0438\u0445', choices=[(b'string', b'string'), (b'int', b'int'), (b'bool', b'bool')]),
            preserve_default=True,
        ),
    ]
