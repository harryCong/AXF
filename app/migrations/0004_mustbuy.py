# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-25 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
    ]
