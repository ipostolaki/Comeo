# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0013_auto_20150703_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='funding_type',
            field=models.CharField(default='unconditional', choices=[('conditional', 'conditional'), ('unconditional', 'unconditional')], max_length=50, verbose_name='Funding type'),
            preserve_default=True,
        ),
    ]
