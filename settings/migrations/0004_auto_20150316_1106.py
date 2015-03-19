# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20150313_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': '\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f', 'verbose_name_plural': '\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f'},
        ),
        migrations.AlterModelOptions(
            name='fieldgroup',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u043f\u043e\u043b\u0456\u0432 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u044c', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u0438 \u043f\u043e\u043b\u0456\u0432 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u044c'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '\u0421\u0435\u043a\u0446\u0456\u044f', 'verbose_name_plural': '\u0421\u0435\u043a\u0446\u0456\u0457'},
        ),
        migrations.AlterModelOptions(
            name='settingsgroup',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u044c', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u0438 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u044c'},
        ),
    ]
