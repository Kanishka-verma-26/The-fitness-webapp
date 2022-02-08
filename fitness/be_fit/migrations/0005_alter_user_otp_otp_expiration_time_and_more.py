# Generated by Django 4.0.1 on 2022-02-08 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('be_fit', '0004_alter_user_otp_otp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otp',
            name='otp_expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 5, 3, 50, 109221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_generate_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 5, 1, 50, 109177, tzinfo=utc)),
        ),
    ]
