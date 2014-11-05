# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0002_auto_20141031_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='dateReglement',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commande',
            name='preuveReglement',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
