# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-18 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Blog Text'),
            preserve_default=False,
        ),
    ]
