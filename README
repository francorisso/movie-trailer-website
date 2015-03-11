## REST APIs

One thing I want to practice here is to build products with a separation between the backend and the frontend. For that I want to use AngularJS for communicating with a Python REST API. For the Python API I'm using Django.

## Where is the code?

All the project is presented in a Django module called "movies" (as the folder who holds the data). There you can find all the code, even the frontend code.


## PROJECT REQUIREMENTS

### Present required content

The page presents all the required content, plus the release date.

### Generate dynamically from Python structure.

The structure I'm using is under /movies/models.py, there is well described how the structure works. For delivering the structure you want to check /urls.py and /movies/urls.py, both of those fields define the routes. Then /movies/views.py manages the actual deliver of the information.

The file /movies/static/app.js and /movies/static/moviesController.js, has the AngularJS code for asking the data and displaying the content in the page.

For the HTML/CSS I'm using bootstrap.

### Page containes errors
I've tested and is error free, however if you find any bugs let me know.

## INSTALL
1. You can start a server from the root of the files, by typing in the command line:

> python manage.py runserver

This will start a server by default in http://127.0.0.1:8000, I've tested the code there.

2. You'll have to change the information in /MovieWeb/settings.py

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : <database_name>,
        'USER'      : <username>, 
        'PASSWORD'  : <pass>, 
        'HOST'      : <host>,
    }
}

3. ...and these paths in the same file (MEDIA_URL is the server you're running):

MEDIA_ROOT = '/Users/macbookpro/Developments/udacity/nanodegree_fullstack_dev/MovieWeb/'
MEDIA_URL = 'http://127.0.0.1:8000/'

4. Now, for creating the database, you've to call from the command line:

> python manage.py makemigrations
> python manage.py migrate

5. For populate the database, I've created a django command that fetches movies from the themoviedb.org, copying images and trailers from the most popular ones, you can run this script as long as you want (limit 10K movies), please see /movies/management/commands/movies_add.py for details of my implementation and if you've any suggestion about this, the idea is run this as a cronjob. 
Back to the instructions, you can run:

> python manage.py movies_add

And this will populate the database.

6. Now go to your browser and type the address you choose for step 1, and is ready.