# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pro_brand_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobapp.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('uname', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=50, null=True)),
                ('phno', models.IntegerField(blank=True, default=None, max_length=12, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pro_brand_map',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobapp.product'),
        ),
    ]
