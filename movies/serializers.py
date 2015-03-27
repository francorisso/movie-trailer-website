from django.forms import widgets
from rest_framework import serializers
from movies.models import Movie
from movies.models import MovieGenres
from datetime import datetime


class MovieGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MovieGenres
        fields = ( 
            'id', 
            'name', 
            'url',
        )

class MovieSerializer(serializers.ModelSerializer):
    genres = MovieGenresSerializer(many=True, read_only=True)

    class Meta:
        model  = Movie
        fields = ( 
            'id', 
            'title', 
            'url',
            'story_line', 
            'description', 
            'poster_image_url',
            'trailer_youtube_url',
            'released_date',
            'updated_date',
            'genres',
        )
