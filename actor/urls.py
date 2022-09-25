from django.urls import path

from actor.views import CelebrityDetailView, AllCelebrityView, CelebrityDOBMonthView, PopularCelebritiesView
# from actor.views import ActorView, ActorDetailView

urlpatterns = [
    path('celebrities/', AllCelebrityView.as_view(), name='celebrities'),
    path('celebrity/<int:pk>', CelebrityDetailView.as_view(), name='celebrity-detail'),
    path('celebrities-today-dob/', CelebrityDOBMonthView.as_view(), name='celebrities-dob-month'),
    path('popular-celebs/', PopularCelebritiesView.as_view(), name='popular-celebs'),

]