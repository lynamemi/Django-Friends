# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0002_auto_20160825_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friendsfriend', to='loginreg.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usersfriend', to='loginreg.User')),
            ],
        ),
    ]