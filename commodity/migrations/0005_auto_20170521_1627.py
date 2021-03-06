# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0004_auto_20170514_0152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commondity',
            options={'ordering': ['-CommodityDateTime'], 'verbose_name': '商品', 'verbose_name_plural': '所有商品'},
        ),
        migrations.AddField(
            model_name='commondity',
            name='CommondityContactMobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommodityCategory',
            field=models.CharField(blank=True, max_length=50, verbose_name='商品类别'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommodityContent',
            field=models.TextField(blank=True, null=True, verbose_name='商品说明'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommodityDateTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='登记日期'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommodityName',
            field=models.CharField(max_length=100, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommodityPrice',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='commondity',
            name='CommondityImage',
            field=models.ImageField(default='static/upload/None/no-img.jpg', upload_to='static', verbose_name='商品图片'),
        ),
    ]
