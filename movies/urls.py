from django.conf.urls import patterns, url
from movies import views

# this are the routes used here, one for get the list, the other for the detail
urlpatterns = patterns('',
    url(r'^$', views.MovieList.as_view(), name='list'),
    url(r'genres', views.Genres.as_view(), name='genres'),
    url(r'^(?P<title_url>[a-zA-Z0-9_-]+)', views.MovieDetail.as_view(), name='detail'),
)