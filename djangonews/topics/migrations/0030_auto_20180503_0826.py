# Generated by Django 2.0.3 on 2018-05-03 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0029_auto_20180430_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 3, 8, 26, 27, 927782, tzinfo=utc)),
        ),
    ]