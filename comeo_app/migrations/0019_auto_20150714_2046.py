# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0018_auto_20150712_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='owner',
        ),
        migrations.AddField(
            model_name='campaign',
            name='editors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='campaign editors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='main_owner',
            field=models.OneToOneField(verbose_name='campaign owner', to=settings.AUTH_USER_MODEL, related_name='campaign_main_owner', null=True),
            preserve_default=True,
        ),
    ]
