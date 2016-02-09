# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthlyinterface', '0005_auto_20160126_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creation',
            old_name='filePath',
            new_name='filer_path',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='filePath',
            new_name='file_path',
        ),
        migrations.AddField(
            model_name='material',
            name='source_url',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
