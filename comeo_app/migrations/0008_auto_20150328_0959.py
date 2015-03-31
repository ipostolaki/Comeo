# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0007_auto_20150327_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='comeouser',
            name='profile',
            field=models.OneToOneField(null=True, to='comeo_app.Profile'),
            preserve_default=True,
        ),
    ]
