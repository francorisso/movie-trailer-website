from movies.models import Movie
from movies.models import MovieGenres
from movies.serializers import MovieSerializer
from movies.serializers import MovieGenresSerializer

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import viewsets, routers
from rest_framework import permissions
from rest_framework.response import Response

'''
Basic index page with styles
'''
def index( request ):

	# I can pass a dictionary with values for use in the view
	context = {}

	return render( request, 'movies/index.html', context)

def getJPEG(request):
    return HttpResponse(getImg.simple(), mimetype="image/jpg")


class Genres(generics.ListCreateAPIView):
	queryset = MovieGenres.objects.all()
	serializer_class = MovieGenresSerializer

'''
API for deliver movies list
'''
class MovieList( generics.ListCreateAPIView ):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

	def list(self, request):
		page 		= int(self.request.GET.get("page"));
		genre_url 	= self.request.GET.get("genre_url");
		show 		= 30
		offset 		= show * page
		limit		= offset + show

		genre = None
		if genre_url:
			genre = MovieGenres.objects.get(url=genre_url)

		queryset   = Movie.objects.all()
		if genre:
			queryset = queryset.filter( genres__id=genre.id )

		queryset = queryset[offset:limit]

		serializer = MovieSerializer(queryset, many=True)

		return Response( serializer.data )



'''
API for deliver details about a movie
'''
class MovieDetail( generics.RetrieveAPIView ):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

	def retrieve(self, request, title_url):
		queryset   	= Movie.objects.get( url = title_url )
		serializer 	= MovieSerializer( queryset )
		return Response( serializer.data )

