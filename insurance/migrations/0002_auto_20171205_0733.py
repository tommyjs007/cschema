# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-05 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='json_schema',
            new_name='schema',
        ),
    ]
