# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0013_artist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=1, upload_to='artist/images/'),
            preserve_default=False,
        ),
    ]