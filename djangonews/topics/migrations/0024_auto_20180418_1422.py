# Generated by Django 2.0.3 on 2018-04-18 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0023_auto_20180418_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 14, 22, 26, 264525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 14, 22, 26, 263550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 18, 14, 22, 26, 265454, tzinfo=utc)),
        ),
    ]