import os

from .settings_deployment import *

# http://rapidsms.readthedocs.io/en/develop/ref/settings.html#installed-backends
INSTALLED_BACKENDS = {
    # From: https://github.com/rapidsms/rapidsms/tree/develop/rapidsms/backends/database
    'message_tester': {
        'ENGINE': 'rapidsms.backends.database.DatabaseBackend',
    },
    # From: https://rapidsms-twilio.readthedocs.io/en/latest/quick-start.html
    "twilio-backend": {
        "ENGINE": "rtwilio.outgoing.TwilioBackend",
        'config': {
            'account_sid': ACCOUNT_SID, 
            'auth_token': AUTH_TOKEN,  
            'number': TWILIO_NUMBER, 
            # optional callback URL
            # 'callback': 'http://<public-django-instance>/backend/twilio/status-callback/',
        }
    },
}

INSTALLED_APPS = [
    'rapidsms',
    # third party apps.
    'django_tables2',
    'selectable',
    'decisiontree',
    'rtwilio',
    # django contrib apps
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    # rapidsms contrib apps.
    'rapidsms.contrib.handlers',
    'rapidsms.contrib.httptester',
    'rapidsms.contrib.messagelog',
    'rapidsms.contrib.messaging',
    'rapidsms.contrib.registration',
    'rapidsms.contrib.echo',
    'rapidsms.router.db',
    'rapidsms.backends.database',
    'rapidsms.backends.kannel',
    'rapidsms.tests.translation',

    'rapidsms.contrib.default',  # Should be last
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

RAPIDSMS_HANDLERS = (
    'rapidsms.contrib.echo.handlers.echo.EchoHandler',
    'rapidsms.contrib.echo.handlers.ping.PingHandler',
)

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'

ROOT_URLCONF = 'coordinated-entry-screening.urls'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        }
    },
    'root': {
        'handlers': ['null'],
    },
    'loggers': {
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

# TBD
# DECISIONTREE_SESSION_END_TRIGGER = 'done'