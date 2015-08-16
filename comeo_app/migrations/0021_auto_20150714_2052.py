# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0020_auto_20150714_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='editors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='campaign_editors', verbose_name='campaign editors'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='owner',
            field=models.OneToOneField(verbose_name='campaign owner', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
