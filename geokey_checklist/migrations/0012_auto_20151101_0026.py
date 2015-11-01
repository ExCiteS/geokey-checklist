# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0011_auto_20151101_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='pertype',
            field=models.CharField(default=b'person', max_length=100, choices=[(b'person', b'Per Person'), (b'household', b'Per Household')]),
        ),
    ]
