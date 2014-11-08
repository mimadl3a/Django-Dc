# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255, blank=True)),
                ('prenom', models.CharField(max_length=255, blank=True)),
                ('username', models.CharField(max_length=255, blank=True)),
                ('password', models.CharField(max_length=255, blank=True)),
                ('isActive', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
