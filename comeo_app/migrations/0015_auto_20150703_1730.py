# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0014_auto_20150703_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='desc_preview',
            field=models.TextField(max_length=400, verbose_name='Short description'),
            preserve_default=True,
        ),
    ]
