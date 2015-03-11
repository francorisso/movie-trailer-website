from django.conf.urls import patterns, include, url
from django.contrib import admin
from movies import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

	url(r'^movies__posters/(?P<path>.*)$',
    'django.views.static.serve', {'document_root': settings.STATIC_MOVIE_POSTERS }),

	url(r'^api/v1/movies/?', include('movies.urls', namespace="movies")),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^/?', views.index, name="index"),
)