# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-09-05 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbforum', '0008_auto_20200905_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lbforumuserprofile',
            name='friends',
            field=models.CharField(default='[]', max_length=2000),
        ),
    ]
