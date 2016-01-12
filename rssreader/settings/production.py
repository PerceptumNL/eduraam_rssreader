from .default import *

DEBUG = bool(int(os.environ.get('DEBUG_FLAG', '0')))

ADMINS = (
    ('Sander', 'sander@perceptum.nl'),
)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {"default": dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ.get('SECRET_KEY')

if 'SITE_ID' in os.environ:
    SITE_ID = int(os.environ.get('SITE_ID'))

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
SERVER_EMAIL = 'rssreader@perceptum.nl'
