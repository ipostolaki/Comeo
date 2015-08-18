# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    replaces = [('comeo_app', '0001_initial'), ('comeo_app', '0002_auto_20150318_1313'), ('comeo_app', '0003_auto_20150321_1508'), ('comeo_app', '0004_auto_20150323_1744'), ('comeo_app', '0005_auto_20150323_2331'), ('comeo_app', '0006_comeouser'), ('comeo_app', '0007_auto_20150327_1722'), ('comeo_app', '0008_auto_20150328_0959'), ('comeo_app', '0009_auto_20150401_2017'), ('comeo_app', '0010_auto_20150414_0802'), ('comeo_app', '0011_emailsub'), ('comeo_app', '0012_auto_20150429_1641'), ('comeo_app', '0013_auto_20150703_1602'), ('comeo_app', '0014_auto_20150703_1714'), ('comeo_app', '0015_auto_20150703_1730'), ('comeo_app', '0016_auto_20150703_1936'), ('comeo_app', '0017_auto_20150703_2017'), ('comeo_app', '0018_auto_20150712_1347'), ('comeo_app', '0019_auto_20150714_2046'), ('comeo_app', '0020_auto_20150714_2049'), ('comeo_app', '0021_auto_20150714_2052'), ('comeo_app', '0022_auto_20150714_2055'), ('comeo_app', '0023_auto_20150722_1617'), ('comeo_app', '0024_auto_20150723_2327'), ('comeo_app', '0025_auto_20150723_2333'), ('comeo_app', '0026_transaction_confirmed')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('bank_account', models.CharField(blank=True, verbose_name='bank account', max_length=300)),
                ('buletin_number', models.CharField(blank=True, verbose_name='buletin number', max_length=50)),
                ('photo', models.FileField(upload_to='users_photos', blank=True, verbose_name='photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComeoUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(unique=True, verbose_name='Email', max_length=254)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', related_query_name='user', related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', related_query_name='user', related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.')),
                ('profile', models.OneToOneField(to='comeo_app.Profile', null=True, verbose_name='user profile')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailSub',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('source', models.CharField(blank=True, verbose_name='source', max_length=300)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('desc_main', models.TextField(verbose_name='Description')),
                ('desc_preview', models.CharField(verbose_name='Preview', max_length=550)),
                ('desc_headline', models.CharField(verbose_name='Headline', max_length=300)),
                ('duration', models.PositiveSmallIntegerField()),
                ('summ_goal', models.PositiveIntegerField()),
                ('collected_summ', models.PositiveIntegerField()),
                ('image_main', models.ImageField(upload_to='campaigns_images', blank=True, verbose_name='Campaign image')),
                ('state', models.CharField(default='draft', verbose_name='State', choices=[('draft', 'draft'), ('public', 'public'), ('complete', 'complete')], max_length=50)),
                ('funding_type', models.CharField(verbose_name='Funding type', max_length=50)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='campaign owners')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=models.ManyToManyField(blank=True, to='comeo_app.Tag', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='funding_type',
            field=models.CharField(default='unconditional', verbose_name='Funding type', choices=[('conditional', 'conditional'), ('unconditional', 'unconditional')], max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='desc_preview',
            field=models.TextField(verbose_name='Short description', max_length=400),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='owners',
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
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 16, 36, 11, 493031, tzinfo=utc), verbose_name='start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='collected_summ',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='editors',
            field=models.ManyToManyField(related_name='campaign_editors', to=settings.AUTH_USER_MODEL, verbose_name='campaign editors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='campaign owner'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.PositiveSmallIntegerField()),
                ('method', models.CharField(default='METHOD_CARD', choices=[('METHOD_CARD', 'Bank card'), ('METHOD_TERMINAL', 'Terminal')], max_length=40)),
                ('campaign', models.ForeignKey(to='comeo_app.Campaign')),
                ('payer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('external_id', models.CharField(null=True, max_length=150)),
                ('date_confirmed', models.DateTimeField(null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirmed', models.BooleanField(default=False)),
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
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='date_finish',
            field=models.DateField(null=True, verbose_name='finish date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='date_start',
            field=models.DateField(null=True, verbose_name='start date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='view count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
            preserve_default=True,
        ),
    ]
