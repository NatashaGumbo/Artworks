# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
                ('biography', models.TextField()),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=50)),
                ('category_description', models.TextField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('available', models.BooleanField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artstore.Artist')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artstore.Categorie')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artstore.Image')),
            ],
        ),
    ]