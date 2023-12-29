# Generated by Django 4.2.5 on 2023-10-14 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0030_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='contact',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='complaints',
            old_name='emails',
            new_name='email',
        ),
        migrations.AddField(
            model_name='complaints',
            name='category',
            field=models.CharField(default='mess', max_length=20),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 14, 23, 48, 52, 571136)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='review',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 48, 52, 571136)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 48, 52, 571136)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 14, 23, 48, 52, 571136)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 23, 48, 52, 571136)),
        ),
    ]
