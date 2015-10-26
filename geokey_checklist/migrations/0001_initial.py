# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_admins_contact'),
        ('categories', '0013_auto_20150130_1440'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('quantityfactor', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('expiryfactor', models.IntegerField()),
                ('expiry', models.DateTimeField(null=True)),
                ('haveit', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='categories.Category')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('field', models.ForeignKey(to='categories.Field')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
