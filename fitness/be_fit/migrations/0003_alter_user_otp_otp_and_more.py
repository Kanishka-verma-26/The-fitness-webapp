# Generated by Django 4.0.1 on 2022-02-07 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('be_fit', '0002_user_otp_delete_registered_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otp',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 12, 9, 55, 316694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_generate_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 12, 7, 55, 316638, tzinfo=utc)),
        ),
    ]