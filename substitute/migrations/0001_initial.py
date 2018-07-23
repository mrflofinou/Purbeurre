# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-16 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'catégorie',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nom')),
                ('nutriscore', models.CharField(max_length=10, verbose_name='nutriscore')),
                ('generic_name', models.CharField(max_length=200, verbose_name='nom générique')),
                ('url_picture', models.CharField(max_length=200, verbose_name='image')),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='substitute.Category')),
            ],
            options={
                'verbose_name': 'produit',
            },
        ),
    ]