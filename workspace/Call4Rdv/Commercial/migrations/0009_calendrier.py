# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0008_auto_20141107_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('description', models.CharField(default=b'', max_length=255)),
                ('start', models.CharField(default=b'', max_length=255)),
                ('end', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
