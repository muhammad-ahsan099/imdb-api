# Generated by Django 4.1 on 2022-09-03 17:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('imageurl', models.ImageField(blank=True, upload_to='MovieCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_url', models.ImageField(blank=True, upload_to='Posters/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(default='tt3032400', max_length=10, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('released', models.DateField()),
                ('runtime', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)])),
                ('language', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('metascore', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('imdb_votes', models.BigIntegerField(blank=True, default=0)),
                ('budget', models.BigIntegerField(blank=True, default=0)),
                ('box_office', models.BigIntegerField(blank=True, default=0)),
                ('imdb_original', models.BooleanField(default=False)),
                ('prime_video', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Movie', 'Movie'), ('TV Show', 'TV Show'), ('Season', 'Season')], max_length=10)),
                ('season_title', models.CharField(blank=True, max_length=255)),
                ('season', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('episode', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('poster_url', models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()])),
                ('video_poster_url', models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()])),
                ('video_url', models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()])),
                ('genre', models.ManyToManyField(related_name='genre_movies', to='movies.genre')),
                ('image_gallery', models.ManyToManyField(blank=True, to='movies.imagegallery')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('review_body', models.TextField(blank=True, max_length=1000)),
                ('is_spoiler', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_poster_url', models.ImageField(blank=True, upload_to='VideoPosters/')),
                ('video_url', models.TextField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='ReviewLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('unlikes', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_like', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='video_gallery',
            field=models.ManyToManyField(blank=True, to='movies.videogallery'),
        ),
    ]