# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0009_auto_20150401_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comeouser',
            name='email',
            field=models.EmailField(verbose_name='Email', unique=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comeouser',
            name='profile',
            field=models.OneToOneField(null=True, to='comeo_app.Profile', verbose_name='user profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bank_account',
            field=models.CharField(verbose_name='bank account', blank=True, max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='buletin_number',
            field=models.CharField(verbose_name='buletin number', blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(verbose_name='photo', blank=True, upload_to='users_photos'),
            preserve_default=True,
        ),
    ]
