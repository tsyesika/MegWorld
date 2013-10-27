import json
import os

# Config paths
paths = [
    os.path.expanduser(os.environ.get("MEGWORLD_CONFIG", "")),
    os.path.expanduser("~/.megworld_config.json"),
    "megworld_config.json",
]

for config in paths:
    if os.path.isfile(config):
        try:
            config = json.read(open(config))
        except IOError:
            raise Exception("Can't open file {0}".format(config))
        except ValueError:
            raise Exception("Can't parse config {0}".format(config))
        finally:
            break

if not isinstance(config, dict):
    config_paths = [path for path in paths if path]
    raise Exception("No configuration found, please place a config in one of {0}".format(", ".join(config_paths)))

DEBUG = config.get("debug", True)
TEMPLATE_DEBUG = DEBUG
ADMINS = config.get("admins", tuple())
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "database.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
    }
}

for name, value in config.get("database", {}):
    name = name.upper()
    DATABASES["default"][name] = value


ALLOWED_HOSTS = config.get("hosts", [])
TIME_ZONE = config.get("timezone", "UTC")
LANGUAGE_CODE = config.get("language", "en-gb")
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = config.get("media", {}).get("path", "/media/")
MEDIA_URL = config.get("media", {}).get("url", "")
STATIC_ROOT = config.get("static", {}).get("path", "")
STATIC_URL = config.get("staitc", {}).get("url", "/static/")
STATICFILES_DIRS = tuple()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = config.get("secret", None)
if SECRET_KEY is None:
    raise Exception("You must define a secret.")

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'megworld.urls'

WSGI_APPLICATION = 'MegWorld.wsgi.application'

TEMPLATE_DIRS = tuple()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.admin',
    'MegWorld',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
