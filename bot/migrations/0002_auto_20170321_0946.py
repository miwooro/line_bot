# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('echobot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='name',
            new_name='event',
        ),
    ]