# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=30)),
                ('mobile_number', models.IntegerField(unique=True, max_length=10)),
                ('year', models.CharField(max_length=1, choices=[(b'1', b'FIRST YEAR'), (b'2', b'SECOND YEAR'), (b'3', b'THIRD YEAR'), (b'4', b'FOURTH YEAR')])),
                ('hostel_name', models.CharField(max_length=1, choices=[(b'Y', b'YASHODHARA BHAVAN'), (b'K', b'KALPANA BHAVAN'), (b'V', b'VRINDAVAN BHAVAN'), (b'S', b'SAKET BHAVAN'), (b'P', b'PANCHAVATI BHAVAN'), (b'J', b'JAYBHARAT BHAVAN')])),
            ],
        ),
    ]
