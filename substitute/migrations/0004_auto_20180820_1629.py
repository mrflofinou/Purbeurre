# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substitute', '0003_auto_20180820_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.BigIntegerField(null=True, unique=True, verbose_name='code produit'),
        ),
    ]
