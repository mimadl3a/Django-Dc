# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_auto_20141126_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='nom',
            field=models.CharField(help_text=b'Ceci est un help text', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
