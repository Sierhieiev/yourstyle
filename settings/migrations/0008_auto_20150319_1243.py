# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gfklookupwidget.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_auto_20150317_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='object_id',
            field=gfklookupwidget.fields.GfkLookupField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
