# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-09-05 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbforum', '0002_auto_20160811_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='lbforumuserprofile',
            name='classes',
            field=models.CharField(default='[]', max_length=10000),
        ),
        migrations.AddField(
            model_name='lbforumuserprofile',
            name='friends',
            field=models.CharField(default='[{"userid": 1, "username": 111}, {"userid": 2, "username": 222}]', max_length=10000),
        ),
    ]