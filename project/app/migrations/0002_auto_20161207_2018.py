# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
