# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0012_auto_20150429_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('desc_main', models.TextField(verbose_name='Description')),
                ('desc_preview', models.CharField(max_length=550, verbose_name='Preview')),
                ('desc_headline', models.CharField(max_length=300, verbose_name='Headline')),
                ('duration', models.PositiveSmallIntegerField()),
                ('summ_goal', models.PositiveIntegerField()),
                ('collected_summ', models.PositiveIntegerField()),
                ('image_main', models.ImageField(upload_to='campaigns_images', verbose_name='Campaign image', blank=True)),
                ('state', models.CharField(choices=[('draft', 'draft'), ('public', 'public'), ('complete', 'complete')], default='draft', max_length=50, verbose_name='State')),
                ('funding_type', models.CharField(max_length=50, verbose_name='Funding type')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('owners', models.ManyToManyField(verbose_name='campaign owners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=models.ManyToManyField(blank=True, verbose_name='Tags', to='comeo_app.Tag'),
            preserve_default=True,
        ),
    ]
