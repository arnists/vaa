# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='ssn',
            field=models.CharField(default='000000-0000', max_length=11),
            preserve_default=False,
        ),
    ]
