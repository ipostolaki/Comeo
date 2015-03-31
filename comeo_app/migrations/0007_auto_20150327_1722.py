# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0006_comeouser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='info',
        ),
        migrations.AddField(
            model_name='profile',
            name='bank_account',
            field=models.TextField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='buletin_number',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comeouser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name'),
            preserve_default=True,
        ),
    ]
