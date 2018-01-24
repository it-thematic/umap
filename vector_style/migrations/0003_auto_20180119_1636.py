# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vector_style', '0002_datalayerstyles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalayerstyles',
            name='datalayer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaflet_storage.DataLayer', verbose_name='Слой'),
        ),
    ]
