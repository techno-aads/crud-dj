# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='isArrive',
            new_name='hasAd',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='address',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='count',
        ),
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.CharField(default=b'description', max_length=300),
        ),
        migrations.AddField(
            model_name='goods',
            name='duration',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(default=b'name', max_length=300),
        ),
    ]
