# Generated by Django 4.1 on 2022-09-03 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='season_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
