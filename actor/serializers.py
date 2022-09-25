from asyncore import read
from dataclasses import fields
from pickletools import read_long1
from rest_framework import serializers
from actor.models import Celebrity, CelebrityRole
# from movies.serializers import MovieSerializer


class CelebrityRoleSerializer(serializers.ModelSerializer):
    celebrity = serializers.StringRelatedField(read_only=True)
    # movie = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CelebrityRole
        fields = ['id', 'director', 'writer',
                  'producer', 'actor', 'celebrity']


class CelebritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Celebrity
        fields = '__all__'


class CelebrityDetailSerializer(serializers.ModelSerializer):
    celebrity = CelebrityRoleSerializer(many=True, read_only=True)

    class Meta:
        model = Celebrity
        fields = ['id', 'name', 'avatar', 'birth_name', 'rank', 'gender', 'birth_place', 'description', 'height',
                  'dob', 'is_married', 'celebrity']
