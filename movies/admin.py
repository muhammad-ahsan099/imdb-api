from django.contrib import admin
from movies.models import ImageGallery, Movie, Genre, Rating, Review, ReviewLikes, VideoGallery


# admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(ReviewLikes)


@admin.register(Movie)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'imdb_id', 'title', 'year',
                    'imdb_rating', 'imdb_votes', 'imdb_original', 'metascore', 'prime_video', 'season_title', 'season', 'episode')


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'poster_url')


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_poster_url')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ratings', 'user', 'movie')
