# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myobject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myobject',
            name='dom',
            field=models.BooleanField(default=False, verbose_name='Дом'),
        ),
    ]
