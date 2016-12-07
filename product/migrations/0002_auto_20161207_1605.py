# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
