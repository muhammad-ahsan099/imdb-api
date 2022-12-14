# Generated by Django 4.1 on 2022-09-10 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 10, 10, 6, 14, 500101)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
