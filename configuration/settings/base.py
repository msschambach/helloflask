# Statement for enabling the development environment
DEBUG = False
ASSETS_DEBUG = False

# Define the source directory
import os

from configuration import BASE_DIR, CONFIG_DIR, SETTINGS_DIR

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Password hashing algorithm
SECURITY_PASSWORD_HASH = 'sha512_crypt'

# Password salt if using HMAC
SECURITY_PASSWORD_SALT = 'aSalty_Phras3%'

# Set whether anyone can register
SECURITY_REGISTERABLE = True

# Set whether someone should be confirmed when they register
SECURITY_CONFIRMABLE = True

# Set whether passwords should be recoverable
SECURITY_RECOVERABLE = True

# Email address to send emails as
SECURITY_EMAIL_SENDER = ''

# Security url prefix for flask security
SECURITY_URL_PREFIX = '/auth'

# Mail configuration
MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'your-smtp-username'
MAIL_PASSWORD = 'your-smtp-password'

# Celery configuration
CELERY_RESULT_BACKEND = ''
CELERY_BROKER_URL = ''
