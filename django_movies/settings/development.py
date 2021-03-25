from django_movies.settings.production import *

# DATABASE DEV
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movies',
        'OPTIONS': {
            'options': '-c search_path=django,public'
        },
        'USER': 'movies',
        'PASSWORD': 'movies',
        'HOST': 'django_movies_db',
        'PORT': '5432',
    }
}