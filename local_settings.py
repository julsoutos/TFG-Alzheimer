
# Modules in use, commented modules that you won't use

ALLOWED_HOSTS = ['localhost' ,'127.0.0.1']


MODULES = [
  'principal',
  'authentication',
  'administrator',
  'doctor',
  'patient'
]
AUTH_USER_MODEL = 'principal.User'

BASEURL = 'http://localhost:8000'

APIS = {
    'principal':BASEURL,
     'authentication':BASEURL,
      'administrator':BASEURL,
      'doctor': BASEURL,
      'patient': BASEURL
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cognitya',
        'USER': 'postgres',
	'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256