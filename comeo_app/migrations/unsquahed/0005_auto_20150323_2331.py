# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0004_auto_20150323_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
