# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0023_auto_20150722_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='external_id',
            field=models.CharField(max_length=150, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
            preserve_default=True,
        ),
    ]
