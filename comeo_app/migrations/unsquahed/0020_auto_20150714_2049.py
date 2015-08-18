# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0019_auto_20150714_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='main_owner',
            new_name='owner',
        ),
    ]
