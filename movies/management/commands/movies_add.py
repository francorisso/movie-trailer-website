from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from slugify import slugify
import requests
import json
import time

from movies.models import Movie
from movies.models import MovieGenres

'''
This cronjob will get movies from themoviedb.org
'''
class Command(BaseCommand):
    can_import_settings = True
    api_endpoint = "http://api.themoviedb.org/3"
    api_key = "cf847f4d1687c247077b506d618db172"
    imgConfig = {}
    IMAGE_DIR = "/movies/static/movies/images/"

    def handle(self, *args, **options):
        self.getTopRated()
    
    def getTopRated(self):
        #get configuration of the API for image paths
        self.imgConfig = self.createRequest( "get", "/configuration", {
            "api_key" : self.api_key,
        })
        self.imgConfig = self.imgConfig["images"]

        for page in range(1,1000):
            response = self.createRequest( "get", "/movie/top_rated", {
                "api_key" : self.api_key,
                "page"    : page
            })
            self.createMovie( response )

    def createMovie(self, response):
        # save results in the database
        for rawitem in response['results']:
            # avoid request limits
            time.sleep(1)

            print "Saving %s" % rawitem['title']
            
            # ask for details about the movie
            item = self.createRequest( "get", "/movie/%s" % rawitem['id'], {
                "api_key" : self.api_key,
                "append_to_response" : "videos"
            })
            
            # collect genres ids
            genres = item['genres']
            genresNew = []
            item['genres'] = []
            for genre in genres:
                try:
                    genredb = MovieGenres.objects.get(name=genre['name'])
                except MovieGenres.DoesNotExist:
                    genredb = MovieGenres( name=genre['name'], url=slugify(genre['name']) )
                    genredb.save()

                genresNew.append(genredb.id)
            
            item['url'] = slugify( item['title'] )

            # trailer
            trailer_youtube_url = None
            if "results" in item['videos']: 
                for video in item['videos']['results']:
                    if ( video['type'].lower()=="trailer" and video['site'].lower()=="youtube" ):
                        trailer_youtube_url = video['key']
                        break

            if trailer_youtube_url != None:
                item['trailer_youtube_url'] = trailer_youtube_url
            else:
                continue

            # create/update movie
            try:
                movie = Movie.objects.get( url=item['url'] )
            except Movie.DoesNotExist:
                movie = Movie()
            
            Movie.createFromJSON( movie, item )
            movie.save()

            # add genres
            movie.genres = genresNew
            
            # add image
            movie.poster_image_ext = self.imgConfig['base_url'] + 'w185' + item['poster_path']

            # save
            movie.save()

            print "... Saved"
        


    def createRequest( self, method, endpoint, parameters ):

        if(method=="get"):
            r = requests.get( self.api_endpoint + endpoint, params=parameters)
        elif( method=="post" ):
            r = request.post( self.api_endpoint + endpoint, data=json.dumps(parameters))

        if r.status_code!=200:
            print r.json()
            r.raise_for_status()
            return False

        return r.json()