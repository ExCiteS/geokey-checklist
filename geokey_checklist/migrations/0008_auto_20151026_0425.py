# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_admins_contact'),
        ('geokey_checklist', '0007_auto_20151026_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistsettings',
            name='frequencybeforeexpiration',
            field=models.CharField(default=b'one_week', max_length=100, choices=[(b'one_week', b'one_week'), (b'one_day', b'one_day'), (b'never', b'never')]),
        ),
        migrations.AddField(
            model_name='checklistsettings',
            name='frequencyonexpiration',
            field=models.CharField(default=b'twice', max_length=100, choices=[(b'once', b'once'), (b'twice', b'twice'), (b'never', b'never')]),
        ),
        migrations.AddField(
            model_name='checklistsettings',
            name='project',
            field=models.ForeignKey(default=1, to='projects.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklistsettings',
            name='reminderson',
            field=models.BooleanField(default=True),
        ),
    ]
