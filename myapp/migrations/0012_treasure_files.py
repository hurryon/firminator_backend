# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20160609_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='files',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
