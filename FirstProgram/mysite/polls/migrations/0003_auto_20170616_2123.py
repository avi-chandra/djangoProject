# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170616_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_details',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person_details',
            name='idcardNum',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]