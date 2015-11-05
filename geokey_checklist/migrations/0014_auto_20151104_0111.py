# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0013_auto_20151101_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklistsettings',
            name='frequencybeforeexpiration',
        ),
        migrations.AddField(
            model_name='checklistsettings',
            name='lastremindercheck',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='checklistsettings',
            name='frequencyonexpiration',
            field=models.CharField(default=30, max_length=100, choices=[(30, b'every month'), (60, b'every two months'), (90, b'every three months'), (180, b'every six months'), (365, b'once a year')]),
        ),
    ]
