# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20170402_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
