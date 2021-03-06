# Generated by Django 2.2.5 on 2019-09-10 12:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_ManyToMany_worksheets_20190904_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='solution_release_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 11, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solution',
            field=martor.models.MartorField(default='The solution to this problem is not available yet.', max_length=1000),
        ),
    ]
