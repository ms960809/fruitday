# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-10 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ujifen',
            field=models.IntegerField(default=0, verbose_name='积分'),
        ),
    ]