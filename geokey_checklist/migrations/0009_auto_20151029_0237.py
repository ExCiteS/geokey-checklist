# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0008_auto_20151026_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='checklistitemdescription',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklistitem',
            name='checklistitemurl',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='checklistitemtype',
            field=models.CharField(default=b'Custom', max_length=100, choices=[(b'Essential', b'Essential'), (b'Useful', b'Useful'), (b'Personal', b'Personal'), (b'FixitChildren', b'FixitChildren'), (b'Toddlers', b'Toddlers'), (b'Infants', b'Infants'), (b'Pets', b'Pets'), (b'Custom', b'Custom')]),
        ),
    ]
