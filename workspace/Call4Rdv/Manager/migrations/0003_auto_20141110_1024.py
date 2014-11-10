# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_auto_20141110_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='prenom',
        ),
    ]
