# Movie Trailer Website

This is a project for Udacity's Nanodegree program.

## REST APIs

One thing I want to practice here is to build products with a separation between the backend and the frontend. For that I want to use AngularJS for communicating with a Python REST API. For the Python API I'm using Django.

## Where is the code?

All the project is presented in a Django module called "movies" (as the folder who holds the data). There you can find all the code, even the frontend code.

## INSTALL

### Requirements
* Unix server (OSX or Linux)
* Root access
* Python installed
* MySQL installed

**Install dependencies: Check that the file install-dependencies.sh has permissions to execute and then run:**

> ./install-dependencies.sh

**This will install the modules:**
- pip
- django
- djangorestframework
- markdown
- django-filter
- MySQL-python
- slugify
- requests

**You'll have to change the information in /MovieWeb/settings.py**

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : <database_name>,
        'USER'      : <username>,
        'PASSWORD'  : <pass>,
        'HOST'      : <host>,
    }
}

**...and these paths in the same file (MEDIA_URL is the server you're running):**

MEDIA_ROOT = '/Users/macbookpro/Developments/udacity/nanodegree_fullstack_dev/MovieWeb/'
MEDIA_URL = 'http://127.0.0.1:8000/'

**Now, for creating the database, you've to call from the command line:**

> python manage.py makemigrations
> python manage.py migrate

**For populate the database**, I've created a django command that fetches movies from the themoviedb.org, copying images and trailers from the most popular ones, you can run this script as long as you want (limit 10K movies), please see /movies/management/commands/movies_add.py for details of my implementation and if you've any suggestion about this, the idea is run this as a cronjob.
Back to the instructions, you can run:

> python manage.py movies_add

And this will populate the database.

**You can start a server from the root of the files, by typing in the command line:**

> python manage.py runserver [address] --settings=MovieWeb.settings
> - **address** should be in format IP:post, example: 127.0.0.1:8000

This will start a server by default in http://127.0.0.1:8000, I've tested the code there.
Now go to your browser and type the address you choose and is ready.


## UDACITY'S REQUIREMENTS

### Present required content

The page presents all the required content, plus the release date.

### Generate dynamically from Python structure.

The structure I'm using is under /movies/models.py, there is well described how the structure works. For delivering the structure you want to check /urls.py and /movies/urls.py, both of those fields define the routes. Then /movies/views.py manages the actual deliver of the information.

The file /movies/static/app.js and /movies/static/moviesController.js, has the AngularJS code for asking the data and displaying the content in the page.

For the HTML/CSS I'm using bootstrap.

### Page containes errors
I've tested and is error free, however if you find any bugs let me know.