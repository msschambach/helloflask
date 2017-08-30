import os

CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
SETTINGS_DIR = os.path.abspath(os.path.join(CONFIG_DIR, 'settings'))
BASE_DIR = os.path.abspath(os.path.join(CONFIG_DIR, os.pardir))

# Get environment variables
ENVIRONMENT = os.getenv('FLASK_ENVIRONMENT', 'development')


def configure(app):

    if ENVIRONMENT is None:
        app.config.from_object('configuration.settings')
    else:
        app.config.from_object('configuration.settings.%s' % ENVIRONMENT)