# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0011_emailsub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsub',
            name='email',
            field=models.EmailField(verbose_name='Email', max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailsub',
            name='source',
            field=models.CharField(verbose_name='source', blank=True, max_length=300),
            preserve_default=True,
        ),
    ]
