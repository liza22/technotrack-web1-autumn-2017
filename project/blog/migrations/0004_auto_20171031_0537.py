# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171031_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=['%Y-%m-%d %H:%M']),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=['%Y-%m-%d %H:%M']),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=['%Y-%m-%d %H:%M']),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=['%Y-%m-%d %H:%M']),
        ),
    ]