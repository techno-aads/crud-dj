# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-07 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
