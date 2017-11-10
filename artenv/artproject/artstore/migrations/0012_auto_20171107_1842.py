# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artstore', '0011_auto_20171107_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_title',
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artstore.Product'),
            preserve_default=False,
        ),
    ]