# Generated by Django 3.2.7 on 2023-04-03 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0006_auto_20221024_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 13, 8, 14, 878068)),
        ),
    ]
