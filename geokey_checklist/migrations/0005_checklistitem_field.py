# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0013_auto_20150130_1440'),
        ('geokey_checklist', '0004_checklist_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='field',
            field=models.ForeignKey(default=1, to='categories.Field'),
            preserve_default=False,
        ),
    ]
