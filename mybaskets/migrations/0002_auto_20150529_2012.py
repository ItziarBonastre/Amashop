# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mybaskets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('surname', models.CharField(max_length=50, blank=True)),
                ('adress', models.CharField(max_length=50, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('cp', models.CharField(max_length=10, blank=True)),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('user', models.ForeignKey(default=1, editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
