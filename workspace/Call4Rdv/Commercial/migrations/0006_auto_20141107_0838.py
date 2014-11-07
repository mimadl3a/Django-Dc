# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commercial', '0005_auto_20141105_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adresse',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
