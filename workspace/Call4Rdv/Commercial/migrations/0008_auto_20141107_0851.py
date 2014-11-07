# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0007_auto_20141107_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='rasinSociale',
            new_name='raisonSociale',
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
