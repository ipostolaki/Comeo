# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0008_auto_20150328_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.FileField(upload_to='users_photos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bank_account',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
