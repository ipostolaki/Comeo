# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0024_auto_20150723_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_confirmed',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='external_id',
            field=models.CharField(null=True, max_length=150),
            preserve_default=True,
        ),
    ]
