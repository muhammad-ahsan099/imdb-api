from django.urls import path
from movies.views import GenreMoviesListView, GenreView, IMDBFanFavoriteMoviesView, IMDBOriginalMoviesView, MostPopularMoviesView, MovieView, MovieDetailView, RatingView, RecentReleasedMoviesView, ReviewView, SearchMovies, Top250MoviesView, TopBoxOfficeMoviesView, TopPickMoviesView, RecentUpcomingMoviesView, IMDBPrimeVideosView
urlpatterns = [
    path('home-movies/', MovieView.as_view(), name='movie'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('imdb-most-popular/', MostPopularMoviesView.as_view(), name='movie-most-popular'),
    path('imdb-top-250-movies/', Top250MoviesView.as_view(), name='movie-top250-movies'),
    path('imdb-top-pick/', TopPickMoviesView.as_view(), name='movies-top-picks'),
    path('imdb-original/', IMDBOriginalMoviesView.as_view(),
         name='movies-imdb-original'),
     path('imdb-prime-videos/', IMDBPrimeVideosView.as_view(),
         name='movies-imdb-original'),
    path('imdb-fan-favorites/', IMDBFanFavoriteMoviesView.as_view(),
         name='movies-imdb-fan-favorites'),
    path('recent-released/', RecentReleasedMoviesView.as_view(), name='movies-recent-released'),
    path('recent-upcoming/', RecentUpcomingMoviesView.as_view(), name='movies-upcoming'),
    path('recent-upcoming/', RecentUpcomingMoviesView.as_view(), name='movies-upcoming'),
    path('top-box-office/', TopBoxOfficeMoviesView.as_view(), name='movies-top-box'),
    path('genre/', GenreView.as_view(), name='genre'),
    path('search/title/', GenreMoviesListView.as_view(), name='genre_list'),
    path('search-movies/', SearchMovies.as_view(), name='movies-search'),
    path('review/', ReviewView.as_view(), name='review'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('rating/<int:pk>/', RatingView.as_view(), name='rating-update'),

]
