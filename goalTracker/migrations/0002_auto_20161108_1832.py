# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goalTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
