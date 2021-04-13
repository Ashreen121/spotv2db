# Generated by Django 3.1.5 on 2021-04-13 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_courseitem_datedue'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseitem',
            name='Name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseitem',
            name='DateDue',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 18, 0, 23, 584384), verbose_name='Due date'),
        ),
    ]
