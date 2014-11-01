# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('rasinSociale', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255)),
                ('dateCommande', models.DateTimeField(default=datetime.datetime(2014, 10, 31, 9, 43, 1, 583686))),
                ('dateReglement', models.DateTimeField()),
                ('preuveReglement', models.CharField(max_length=255)),
                ('totalTTC', models.FloatField()),
                ('script', models.TextField()),
                ('nbrRdv', models.IntegerField()),
                ('fichierProspect', models.BooleanField(default=False)),
                ('objections', models.TextField()),
                ('plageHoraire', models.TextField()),
                ('client', models.ForeignKey(to='Commercial.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
