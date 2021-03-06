"""
Django settings for Call4Rdv project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6#7x8f&p+w5l(9z==xp9sputn$gpzplj1d89je3^(ggkjc&3_j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Commercial',
    'Manager',
    'widget_tweaks',
    #'debug_toolbar.apps.DebugToolbarConfig',
    'crispy_forms',
    'fullcalendar',
    'captcha',
    'rest_framework',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


RECAPTCHA_PUBLIC_KEY = '6LcZBf4SAAAAAJtLwXK1Ml7SV7x45ZrLDcw8m7o5'
RECAPTCHA_PRIVATE_KEY = '6LcZBf4SAAAAANqQPiwujvtRODb6AVIwjhJPweQu'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'Call4Rdv.urls'

WSGI_APPLICATION = 'Call4Rdv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CALL4RDV',
        'USER': 'root',
        'PASSWORD': 'imad',
        'HOST': '127.0.0.1',
        'PORT': '3306'
        
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_FROM = 'notifications@data-shore.com'

# These are optional -- if they're set as environment variables they won't
# need to be set here as well
AWS_ACCESS_KEY_ID = 'keys1'
AWS_SECRET_ACCESS_KEY = 'keys2'

# Additionally, you can specify an optional region, like so:
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

CRISPY_TEMPLATE_PACK = "bootstrap3"

STATIC_URL = '/static/'



TEMPLATE_DIRS = (
 '/home/imad/workspace/Call4Rdv/',
)
