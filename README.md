# Eoghy Unscripted

## LinkTree

## Author: Eoghan Hulbert

## Version: 1.0

This Django project was built to be used as a simple, user-customized LinkTree app which would allow a developer to create new functions and features as desired. For example: Themes, Icons, Contact Info, Etc.

### Notes

This app requires a separate `local_settings.py` file which holds the secret key, debug boolean, allowed hosts and database settings. I choose this setup to keep that data hidden when hosting on a server to the public to avoid issues or security threats.

#### local_settings.py File Sample

'''
SECRET_KEY = '8Db[e(c64){}=l*4%3wzsxcl_$$l9e0b!gtf!%g9$7)fmh5y=w7&8'
DEBUG = True/False
ALLOWED_HOSTS = ['site1.local', 'site2.local', 'localhost', '10.0.0.188']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myDB',
        'USER': 'myUserName',
        'PASSWORD': 'myPassword1',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}
'''
