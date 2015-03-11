from django.db import models
from datetime import datetime  
import urllib
import os
from django.core.files import File

'''
This model is for genres of the movies
'''
class MovieGenres( models.Model ):
	name = models.CharField(max_length=200)
	url  = models.CharField(max_length=200)

'''
This model is the main movie object creator.
It uses django Model capacities to build this into the database.
'''
class Movie( models.Model ):
	api_id				= models.IntegerField(default=0)
	revenue				= models.IntegerField(default=0)
	title 				= models.CharField(max_length=200)
	url 				= models.CharField(max_length=200, default=None)
	story_line 			= models.TextField(max_length=1000)
	description 		= models.TextField()
	poster_image_url 	= models.ImageField(upload_to='movies__posters', blank=True)
	poster_image_ext 	= models.URLField()
	trailer_youtube_url = models.CharField(max_length=200)
	released_date		= models.DateField()
	created_date		= models.DateTimeField(
							auto_now=False, 
							auto_now_add=True, 
							default=datetime.now())
	updated_date		= models.DateTimeField(
							auto_now=True, 
							auto_now_add=True, 
							default=datetime.now())

	# relation with foreign keys
	genres 				= models.ManyToManyField(MovieGenres)

	def __str__(self):
		return self.title

	def get_remote_image(self):
		if self.poster_image_ext and not self.poster_image_url:
			result = urllib.urlretrieve( self.poster_image_ext )
			self.poster_image_url.save(
				os.path.basename( self.poster_image_ext ),
				File(open(result[0]))
			)
			self.save()

	def save(self, *args, **kwargs):
		self.get_remote_image()
		super(Movie, self).save(*args, **kwargs)
		

	@staticmethod
	def mapFromMovieDbOrg( field ):
		fields = {
			"title"					: "title",
			"release_date"			: "released_date",
      		"tagline"				: "story_line",
      		"overview"				: "description",
      		"id"					: "api_id",
      		"url"					: "url",
      		"trailer_youtube_url" 	: "trailer_youtube_url"
		}
		if( field in fields):
			return fields[field]

		return False

	'''
	It fills a Movie object from a JSON
	'''
	@staticmethod
	def createFromJSON( movie, parameters ):
		for (field, value) in parameters.items():
			fieldMapped = Movie.mapFromMovieDbOrg(field)
			if(fieldMapped==False):
				continue
			
			setattr(movie, fieldMapped, value)

		return movie
