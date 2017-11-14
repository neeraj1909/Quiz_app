# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20171114_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
