# Generated by Django 2.0.3 on 2018-04-16 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0020_auto_20180413_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 14, 38, 4, 891076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 14, 38, 4, 889640, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 14, 38, 4, 892396, tzinfo=utc)),
        ),
    ]
