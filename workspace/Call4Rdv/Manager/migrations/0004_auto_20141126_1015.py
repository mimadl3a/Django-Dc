# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_auto_20141125_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial',
            name='data',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/imad/workspace/Call4Rdv/Manager/static/media/fichiers'), null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
