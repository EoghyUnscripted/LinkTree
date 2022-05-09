# Eoghy Unscripted

## LinkTree

## Author: Eoghan Hulbert

## Version: 1.0

This Django project was built to be used as a simple, user-customized LinkTree app which would allow a developer to create new functions and features as desired. For example: Themes, Icons, Contact Info, Etc.

### Notes

This app requires a separate `local_settings.py` file which holds the secret key, debug boolean, allowed hosts and database settings. I choose this setup to keep that data hidden when hosting on a server to the public to avoid issues or security threats.

#### local_settings.py File Sample

``` Python
SECRET_KEY = '8Db[e(c64){}=l*4%3wzsxcl_$$l9e0b!gtf!%g9$7)fmh5y=w7&8'    # Never share your secret key
DEBUG = True/False  # Debug should be set False when hosting live, True when developing/testing
ALLOWED_HOSTS = ['site1.local', 'site2.local', 'localhost', '10.0.0.188']   # Include your main URL when hosting live

# This is a sample when using PostGreSql
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
```

In the `settings.py` file, I have scripted code that will import this data from the `local_settings.py` file so that it can remain separate and hidden from malicious actors. See below.

``` Python

try:
    from .local_settings import *
except ImportError:
    pass

```
