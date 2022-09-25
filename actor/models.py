from tkinter.tix import Tree
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie
from django.core.validators import URLValidator


class Celebrity(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=200)
    birth_name = models.CharField(max_length=200, blank=True)
    rank = models.PositiveSmallIntegerField(blank=True, default=0)
    gender = models.CharField(max_length=6, choices=GENDER)
    # avatar = models.ImageField(upload_to='CelebrityGallery/', blank=True)
    avatar = models.TextField(
        validators=[URLValidator()], blank=True, max_length=2000)
    description = models.TextField(blank=True)
    birth_place = models.CharField(max_length=200, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, blank=True)

    is_married = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class CelebrityRole(models.Model):
    celebrity = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE, related_name='celebrity')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='celebrity_role', null=True)
    director = models.BooleanField(default=False)
    writer = models.BooleanField(default=False)
    actor = models.BooleanField(default=False)
    producer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.celebrity.name 
        