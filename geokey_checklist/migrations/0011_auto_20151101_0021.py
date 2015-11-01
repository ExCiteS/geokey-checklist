# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0010_auto_20151029_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='pertype',
            field=models.CharField(default=b'per_person', max_length=100, choices=[(b'per_person', b'Per Person'), (b'per_household', b'Per Household')]),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='checklisttype',
            field=models.CharField(default=b'Blank', max_length=100, choices=[(b'Home', b'Home'), (b'Work', b'Work'), (b'School', b'School'), (b'PlaceOfWorship', b'Place of Worship'), (b'Vehicle', b'Vehicle'), (b'Blank', b'Blank')]),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='checklistitemtype',
            field=models.CharField(default=b'Custom', max_length=100, choices=[(b'Essential', b'Essential'), (b'Useful', b'Useful'), (b'Personal', b'Personal'), (b'Fixit', b'Fix It'), (b'Children', b'Children'), (b'Toddlers', b'Toddlers'), (b'Infants', b'Infants'), (b'Pets', b'Pets'), (b'Custom', b'Custom')]),
        ),
        migrations.AlterField(
            model_name='checklistsettings',
            name='frequencybeforeexpiration',
            field=models.CharField(default=7, max_length=100, choices=[(180, b'six months'), (90, b'three months'), (30, b'one month'), (7, b'one week'), (1, b'one day'), (999999, b'never')]),
        ),
    ]
