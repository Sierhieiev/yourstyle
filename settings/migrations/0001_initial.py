# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('system_name', models.SlugField(max_length=150, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430')),
                ('descriptions', models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441')),
                ('value', models.CharField(max_length=500, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('value_type', models.CharField(max_length=50, verbose_name='\u0422\u0438\u043f \u0434\u0430\u043d\u0438\u0445')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('system_name', models.SlugField(max_length=150, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430')),
                ('descriptions', models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('system_name', models.SlugField(max_length=150, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430')),
                ('descriptions', models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SettingsGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('system_name', models.SlugField(max_length=150, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u043d\u0430\u0437\u0432\u0430')),
                ('descriptions', models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441')),
                ('section', models.ForeignKey(to='settings.Section')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fieldgroup',
            name='section',
            field=models.ForeignKey(to='settings.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldgroup',
            name='settings_group',
            field=models.ForeignKey(to='settings.SettingsGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='field_group',
            field=models.ForeignKey(to='settings.FieldGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='section',
            field=models.ForeignKey(to='settings.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='settings_group',
            field=models.ForeignKey(to='settings.SettingsGroup'),
            preserve_default=True,
        ),
    ]
