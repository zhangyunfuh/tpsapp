# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpsapp', '0006_wheel_trackid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('addr', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
            ],
            options={
                'db_table': 'tpsapp_detail',
            },
        ),
        migrations.AlterField(
            model_name='wheel',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]
