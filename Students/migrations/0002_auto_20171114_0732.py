# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
