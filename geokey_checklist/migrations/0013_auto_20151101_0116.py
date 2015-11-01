# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geokey_checklist', '0012_auto_20151101_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='pertype',
            field=models.CharField(default=b'individual', max_length=100, choices=[(b'individual', b'Per Individual'), (b'location', b'Per Location')]),
        ),
        migrations.AlterField(
            model_name='checklistsettings',
            name='frequencybeforeexpiration',
            field=models.CharField(default=180, max_length=100, choices=[(180, b'six months'), (90, b'three months'), (30, b'one month'), (7, b'one week'), (1, b'one day'), (999999, b'never')]),
        ),
    ]
