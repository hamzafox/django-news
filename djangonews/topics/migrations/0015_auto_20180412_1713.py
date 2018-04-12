# Generated by Django 2.0.3 on 2018-04-12 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0014_auto_20180411_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 12, 17, 13, 4, 373529, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 12, 17, 13, 4, 372707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 12, 17, 13, 4, 374438, tzinfo=utc)),
        ),
    ]