from statistics import mode
from django.db import models
# Create your models here.
# from actor.models import Actor

# from django.utils.text import slugify
# import requests
# from io import BytesIO
# from django.core import files
# from django.urls import reverse
from accounts.models import User
# from actor.models import Actor
from django.core.validators import URLValidator
# from cloudinary_storage.storage import VideoMediaCloudinaryStorage
# from cloudinary_storage.validators import validate_video
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=25)
    imageurl = models.ImageField(upload_to='MovieCategory', blank=True)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    # poster_url = models.ImageField(upload_to='Posters/', blank=True)
    poster_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)
    # def __str__(self):
    #     return self.imageurl


class VideoGallery(models.Model):
    video_poster_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)    # video = models.ImageField(upload_to='Trailers/', blank=True, storage=VideoMediaCloudinaryStorage(),
    #                           validators=[validate_video])
    video_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)

    # def __str__(self):
    #     return self.videoUrl


class Movie(models.Model):
    MOVIE_TYPE = (
        ('Movie', 'Movie'),
        ('TV Show', 'TV Show'),
        ('Season', 'Season')
    )
    imdb_id = models.CharField(
        max_length=10, blank=False, unique=True, default='tt3032400')
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=True)
    released = models.DateField()
    runtime = models.PositiveIntegerField(blank=True, validators=[
        MaxValueValidator(999),
        MinValueValidator(1)
    ])
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    metascore = models.PositiveSmallIntegerField(default=0, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    imdb_votes = models.BigIntegerField(blank=True, default=0)
    budget = models.BigIntegerField(blank=True, default=0)
    box_office = models.BigIntegerField(blank=True, default=0)
    imdb_original = models.BooleanField(default=False)
    prime_video = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=MOVIE_TYPE)
    season_title = models.CharField(max_length=255, blank=True, null=True)
    season = models.PositiveSmallIntegerField(blank=True, default=0)
    episode = models.PositiveSmallIntegerField(blank=True, default=0)
    # poster_url = models.ImageField(upload_to='Posters/', blank=True)
    # video_poster_url = models.ImageField(upload_to='VideoPosters/', blank=True)
    poster_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)
    video_poster_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)
    video_url = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)
    genre = models.ManyToManyField(Genre, related_name='genre_movies')
    image_gallery = models.ManyToManyField(ImageGallery, blank=True)
    video_gallery = models.ManyToManyField(VideoGallery, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Rating(models.Model):
    ratings = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')
    movie = models.ForeignKey(
        Movie, related_name='movie_rating', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' / ' + self.movie.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
    title = models.CharField(max_length=255, blank=True)
    review_body = models.TextField(max_length=1000, blank=True)
    is_spoiler = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ' / ' + self.movie.title


class ReviewLikes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_review_like')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='review_like')
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ' / ' + self.review.title
