# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-14 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0004_auto_20200614_0927'),
        ('fav', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfavouriteshop',
            unique_together=set([('user', 'shop')]),
        ),
    ]