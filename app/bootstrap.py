from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configuration import configure
from configuration.assets import create_assets
from app.manifest import register_modules
from app.exception.handling import handle_errors

# Instantiate app
app = Flask(__name__)

# Configure app
configure(app)

# Initialize assets with app
assets = create_assets(app)
assets.init_app(app)

# Initialize mail
mail = Mail(app)

# Define database object used by modules
db = SQLAlchemy(app)

# Setup migrations
migrate = Migrate(app, db)

# Error handling
handle_errors(app)

# Register modules
register_modules(app)

# Build the database
# This will build the database using SQLAlchemy
db.create_all()
