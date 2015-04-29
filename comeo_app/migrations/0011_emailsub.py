# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0010_auto_20150414_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSub',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('source', models.CharField(max_length=300, verbose_name='source')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
