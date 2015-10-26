# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0006_auto_20151025_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='checklisttype',
            field=models.CharField(default=b'Blank', max_length=100, choices=[(b'Home', b'Home'), (b'Work', b'Work'), (b'School', b'School'), (b'PlaceOfWorship', b'PlaceOfWorship'), (b'Vehicle', b'Vehicle'), (b'Blank', b'Blank')]),
        ),
        migrations.AddField(
            model_name='checklist',
            name='numberofchildren',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='numberofinfants',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='numberofpets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='numberoftoddlers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='checklistitemtype',
            field=models.CharField(default=b'Custom', max_length=100, choices=[(b'Essential', b'Essential'), (b'Useful', b'Useful'), (b'Personal', b'Personal'), (b'Children', b'Children'), (b'Toddlers', b'Toddlers'), (b'Infants', b'Infants'), (b'Pets', b'Pets'), (b'Custom', b'Custom')]),
        ),
    ]
