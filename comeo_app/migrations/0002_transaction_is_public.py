# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0001_squashed_0026_transaction_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
