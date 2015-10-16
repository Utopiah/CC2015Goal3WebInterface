# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('desired_theme', models.CharField(max_length=200, default='unset')),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Desired_Format',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, default='unset')),
            ],
        ),
        migrations.AddField(
            model_name='creation',
            name='desired_format',
            field=models.ForeignKey(to='monthlyinterface.Desired_Format'),
        ),
        migrations.AddField(
            model_name='creation',
            name='parent',
            field=models.ForeignKey(to='monthlyinterface.Creation'),
        ),
    ]
