# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-02 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170202_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_desc',
            field=models.CharField(default='', max_length=700),
        ),
    ]
