# Generated by Django 4.1 on 2022-09-10 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0011_alter_celebrity_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 10, 15, 39, 14, 419142)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celebrity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]