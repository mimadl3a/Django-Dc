# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commercial',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='email',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='id',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='isActive',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='password',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='username',
        ),
        migrations.AddField(
            model_name='commercial',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default='', serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
