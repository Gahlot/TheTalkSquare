# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_topic_topic_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
