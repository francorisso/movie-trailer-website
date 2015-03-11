from django.forms import widgets
from rest_framework import serializers
from movies.models import Movie
from datetime import datetime

class MovieSerializer(serializers.ModelSerializer):
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
            'updated_date'
        )
    