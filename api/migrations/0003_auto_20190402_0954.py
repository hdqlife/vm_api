# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190328_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachine',
            name='vm_datastore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PhysicalDisk'),
        ),
    ]
