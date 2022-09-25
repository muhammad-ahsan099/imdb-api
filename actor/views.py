# Create your views here.
from calendar import month
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from actor.models import Celebrity
# from actor.models import CelebrityDetail
from actor.renderers import ActorRenderer
from actor.serializers import CelebrityDetailSerializer, CelebritySerializer
from datetime import datetime, date, time, timedelta
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters



class AllCelebrityView(APIView):
    # renderer_classes = [ActorRenderer]

    def get(self, request, format=None):
        celebrites = Celebrity.objects.all()
        serializer = CelebritySerializer(
            celebrites, many=True,)
        return Response(
            {
                'message': 'Successfully fetched all celebrities.',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)



class CelebrityDetailView(APIView):
    # renderer_classes = [ActorRenderer]

    def get(self, request, pk, format=None):
        celebrity = Celebrity.objects.get(id=pk)
        serializer = CelebrityDetailSerializer(
            celebrity, context={'request': request})

        return Response(
            {
                'message': 'Successfully fetched celebrity detail.',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)


class CelebrityDOBMonthView(APIView):

    def get(self, request, format=None):
        current_month = datetime.today()
        celebrities = Celebrity.objects.filter(dob__month__exact=current_month.month)

        serializer = CelebritySerializer(celebrities, many=True)
        return Response(
            {
                'message': 'Successfully fetched celebrities with current month birthday.',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            },
            status=status.HTTP_200_OK)



class PopularCelebritiesView(ListAPIView):
    # renderer_classes = [ActorRenderer]
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['rank']