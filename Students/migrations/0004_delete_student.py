# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_auto_20171114_0733'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
