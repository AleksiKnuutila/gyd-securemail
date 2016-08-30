# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securemsg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publickey',
            name='email_address',
            field=models.CharField(default='foo', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publickey',
            name='public_key',
            field=models.CharField(max_length=500),
        ),
    ]
