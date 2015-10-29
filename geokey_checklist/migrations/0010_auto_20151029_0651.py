# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0009_auto_20151029_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='quantityunit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='checklistitemdescription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='checklistitemurl',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
