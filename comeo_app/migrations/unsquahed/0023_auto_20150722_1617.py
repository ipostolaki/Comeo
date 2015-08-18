# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0022_auto_20150714_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField()),
                ('method', models.CharField(max_length=40, choices=[('METHOD_CARD', 'Bank card'), ('METHOD_TERMINAL', 'Terminal')], default='METHOD_CARD')),
                ('campaign', models.ForeignKey(to='comeo_app.Campaign')),
                ('payer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='start_date',
        ),
        migrations.AddField(
            model_name='campaign',
            name='date_created',
            field=models.DateTimeField(verbose_name='creation date', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='date_finish',
            field=models.DateField(verbose_name='finish date', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='date_start',
            field=models.DateField(verbose_name='start date', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='views_count',
            field=models.PositiveIntegerField(verbose_name='view count', default=0),
            preserve_default=True,
        ),
    ]
