# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0016_auto_20150703_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
            preserve_default=True,
        ),
    ]
