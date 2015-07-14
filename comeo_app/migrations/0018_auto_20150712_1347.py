# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0017_auto_20150703_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='collected_summ',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=True,
        ),
    ]
