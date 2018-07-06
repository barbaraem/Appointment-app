# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.SmallIntegerField(max_length=9)),
                ('time', models.DateTimeField()),
                ('time_zone', timezone_field.fields.TimeZoneField(default='Europe/Warsaw')),
                ('task_id', models.CharField(max_length=150, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
