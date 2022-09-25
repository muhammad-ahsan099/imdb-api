from rest_framework import serializers
from actor.serializers import CelebrityDetailSerializer, CelebrityRoleSerializer
# from actor.serializers import CelebrityRoleSerializer
from movies.models import ImageGallery, Movie, Genre, Rating, Review, VideoGallery
# from actor.models import CelebrityDetail


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title', 'imageurl']


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = ['poster_url']


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ['video_poster_url', 'video_url']


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'imdb_id', 'title', 'year', 'description', 'released' ,'poster_url',
                  'video_poster_url', 'imdb_rating','imdb_votes', 'imdb_original', 'metascore','box_office', 'prime_video', 'season_title', 'season','episode', 'genre' ]



class MovieDetailSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True, read_only=True)
    image_gallery = ImageGallerySerializer(many=True, read_only=True)
    video_gallery = VideoGallerySerializer(many=True, read_only=True)
    celebrity_role = CelebrityRoleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreMoviesListSerializer(serializers.ModelSerializer):
    genre_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'title', 'imageurl', 'genre_movies']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['id', 'text', 'spoiler', 'likes', 'unlikes' ]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
