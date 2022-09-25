from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from movies.models import Movie, Genre, Rating, Review
from movies.renderers import MovieRenderer
from movies.serializers import GenreMoviesListSerializer, MovieDetailSerializer, MovieSerializer, GenreSerializer, RatingSerializer, ReviewSerializer
# from accounts.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from .paginations import HomeMoviesResultsSetPagination, MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from datetime import datetime, date, time, timedelta
from rest_framework.exceptions import ValidationError


class MovieView(ListAPIView):
    renderer_classes = [MovieRenderer]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        current_day = datetime.today()
        result = self.queryset.filter(released__gte=current_day -
                                      timedelta(days=30),
                                      released__lte=current_day +
                                      timedelta(days=30)
                                      )
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'Result not found!',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )

class SearchMovies(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']



class Top250MoviesView(ListAPIView):
    renderer_classes = [MovieRenderer]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['-imdb_rating', 'year']


class MostPopularMoviesView(ListAPIView):
    renderer_classes = [MovieRenderer]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['-imdb_rating']

    def get_queryset(self):
        current_year = datetime.today().year
        print(current_year, 'year')
        result = self.queryset.filter(year__exact=current_year)
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'Error in fetching Most popular movies',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )


class TopPickMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['imdb_votes', 'metascore']
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        result = self.queryset.filter(
            imdb_rating__gte=7, metascore__gte=80, imdb_votes__gte=500000)
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'No movies in Top Pick section',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)


class IMDBOriginalMoviesView(ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'imdb_original': ['exact']}
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        result = self.queryset.filter(imdb_original__exact=True)
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'No movies in IMDb Original',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )


class IMDBPrimeVideosView(ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'prime_video': ['exact']}
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        result = self.queryset.filter(prime_video__exact=True)
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'No movies in IMDb Original',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )


class IMDBFanFavoriteMoviesView(ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        result = self.queryset.filter(
            imdb_votes__gt=700000, imdb_rating__gte=7)
        if result.exists():
            return result
        raise ValidationError(
            {
                'message': 'No movies in Fan Favorites',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )

    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)


class RecentReleasedMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        current_day = datetime.today()
        movies = self.queryset.filter(
            released__lt=current_day, released__gt=current_day-timedelta(days=30))
        if movies.exists():
            return movies
        raise ValidationError(
            {
                'message': 'No movies to Upcoming',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )


class RecentUpcomingMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = HomeMoviesResultsSetPagination

    def get_queryset(self):
        current_day = datetime.today()
        movies = self.queryset.filter(
            released__gt=current_day, released__lt=current_day+timedelta(days=30))

        if movies.exists():
            return movies
        raise ValidationError(
            {
                'message': 'No movies in Recent',
                'success': False,
                'status': status.HTTP_404_NOT_FOUND,
            }
        )




class MovieDetailView(APIView):
    renderer_classes = [MovieRenderer]

    def get(self, request, pk, format=None):
        movies = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(
            movies, context={'request': request})
        return Response(
            {
                'message': 'Successfully fetched movie detail.',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)


class GenreView(APIView):

    def get(self, request, format=None):
        genre = Genre.objects.all()
        serializer = GenreSerializer(
            genre, many=True, context={'request': request})
        return Response(
            {
                'message': 'Successfully fetched genre list',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)


class GenreMoviesListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreMoviesListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'title': ['in']}



class ReviewView(APIView):
    renderer_classes = [MovieRenderer]

    def get(self, request, format=None):
        print('request: ', request.data)
        movie_id = request.data['movieId']
        reviews = Review.objects.filter(movie=movie_id)
        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(
            {
                'message': 'Successfully fetched Reviews',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ReviewSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': 'Review Added Successfully',
                'success': True,
                'status': status.HTTP_201_CREATED,
            },
            status=status.HTTP_201_CREATED)

    def patch(self, request, format=None):
        review_id = request.data['id']
        review = Review.objects.get(id=review_id)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': 'Review Updated Successfully',
                'success': True,
                'status': status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK)


class RatingView(APIView):
    renderer_classes = [MovieRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = RatingSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {
                'message': 'Ratings to Movie Added Successfully',
                'success': True,
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        rating = Rating.objects.get(id=pk)
        serializer = RatingSerializer(
            rating, data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {
                'message': 'Ratings Updated Successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        rating = Rating.objects.get(id=pk)
        rating.delete()
        return Response(
            {
                'message': 'Ratings Deleted Successfully',
                'success': True,
                'status': status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK)
