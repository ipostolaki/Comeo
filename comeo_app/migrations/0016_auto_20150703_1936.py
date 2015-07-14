# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0015_auto_20150703_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='owners',
        ),
        migrations.AddField(
            model_name='campaign',
            name='owner',
            field=models.ManyToManyField(verbose_name='campaign owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='collected_summ',
            field=models.PositiveIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date', default=datetime.datetime(2015, 7, 3, 16, 36, 11, 493031, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
