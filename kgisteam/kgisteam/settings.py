"""
Django settings for kgisteam project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from dotenv import load_dotenv
import os
import re


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load env files using paths based on BASE_DIR.
"""
https://github.com/theskumar/python-dotenv

Environmental variables:
    Variables are stored in the .env_settings file.
    Required variables are called with os.environ['ENV_VAL'].
    Optional variables are called with os.getenv('ENV_VAL').

Example .env file for debugging:
    export LOCAL=1
    export DEBUG=1
    export SECRET_KEY='You will never guess, that this is only a test!'
"""
settings_dotenv = os.path.join(BASE_DIR, 'kgisteam', '.env_settings')
if not os.path.isfile(settings_dotenv):
    print('\n\tNo dot env file found at {}'.format(settings_dotenv))
    print('\tDetails in {}\n'.format(os.path.abspath(__file__)))
    exit(0)
load_dotenv(dotenv_path=settings_dotenv, verbose=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

if DEBUG:
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
    ]
else:
    ALLOWED_HOSTS = [
        'www.kgisteam.com',
    ]



# Application definition

INSTALLED_APPS = [
    'courses.apps.CoursesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.forms',
    'info.apps.InfoConfig',
    'markdownx',
    'taggit',
    'users.apps.UsersConfig',
    'utils.apps.UtilsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # BEGIN django-htmlmin middleware
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    # END django-htmlmin middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kgisteam.urls'

IGNORABLE_404_URLS = [
    re.compile(r'\.(php|xml)$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^\robots\.txt'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/2.2/howto/overriding-templates/
        'DIRS': [
            os.path.join(BASE_DIR, 'kgisteam/templates'),
            os.path.join(BASE_DIR, 'template_overrides'),
         ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kgisteam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if os.environ.get('MYSQL_ENGINE'):
    DATABASES = {
        'default': {
            'ENGINE': os.environ['MYSQL_ENGINE'],
            'NAME': os.environ['MYSQL_NAME'],
            'USER': os.environ['MYSQL_USER'],
            'PASSWORD': os.environ['MYSQL_PASSWORD'],
            'HOST': os.environ['MYSQL_HOST'],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('MYSQL_ENGINE', default='django.db.backends.sqlite3'),
            'NAME': os.environ.get('MYSQL_NAME', default=os.path.join(BASE_DIR, 'db_for_testing.sqlite3')),
            }
        }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    'kgisteam/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

# Adding settings to the default: Settings are in alphabetical order.
AUTH_USER_MODEL = 'users.CustomUser'

# https://docs.djangoproject.com/en/2.2/ref/forms/renderers/#django.forms.renderers.TemplatesSetting
'''
Allows widget override for markdownx.
docs: https://neutronx.github.io/django-markdownx/customization/
custom template: templates/markdownx/widget2.html
'''
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

# django-taggit settings
TAGGIT_CASE_INSENSITIVE = True

# security settings
if not os.getenv('LOCAL'):
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    X_FRAME_OPTIONS = 'DENY'
