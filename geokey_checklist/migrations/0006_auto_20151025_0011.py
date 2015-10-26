# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0005_checklistitem_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChecklistCategory',
        ),
        migrations.DeleteModel(
            name='ChecklistType',
        ),
        migrations.AddField(
            model_name='checklistitem',
            name='checklistitemtype',
            field=models.CharField(default=b'Custom', max_length=100, choices=[(b'Essential', b'Essential'), (b'Useful', b'Useful'), (b'Personal', b'Personal'), (b'Kids', b'Kids'), (b'Pets', b'Pets'), (b'Custom', b'Custom')]),
        ),
    ]
