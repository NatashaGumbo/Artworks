# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0004_auto_20171105_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_title', models.CharField(max_length=50)),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]