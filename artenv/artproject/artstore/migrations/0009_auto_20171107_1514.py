# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0008_auto_20171107_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_title',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=1, upload_to='images/products/'),
            preserve_default=False,
        ),
    ]