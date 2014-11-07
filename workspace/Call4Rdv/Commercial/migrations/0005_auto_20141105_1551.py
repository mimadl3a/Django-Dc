# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0004_auto_20141105_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='rasinSociale',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
