# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-02 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='performer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='songs.Performer'),
        ),
    ]
