# Generated by Django 2.0.3 on 2018-04-10 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_auto_20180410_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 10, 16, 25, 53, 180668, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 10, 16, 25, 53, 181342, tzinfo=utc)),
        ),
    ]
