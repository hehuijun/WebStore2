# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0007_merge_20170523_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commondity',
            name='Mobile',
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommondityImage',
            field=models.ImageField(default='static/no-img.jpg', upload_to='static', verbose_name='商品图片'),
        ),
    ]
