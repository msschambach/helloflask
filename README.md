# Hello Flask
A simple flask application

## Development
1. Create a virtualenv: `virtualenv -p python3 .venv`
2. Activate virtualenv: `source .venv/bin/activate`
3. Install requirements: `pip installl -r requirements/development.txt`

While developing, run `python run.py` on your terminal to start the development server.

## Staging and Production
To run the app on staging or production environments run:
`FLASK_APP=run.py FLASK_ENVIRONMENT=staging flask run` and
`FLASK_APP=run.py FLASK_ENVIRONMENT=production flask run` respectively.

Make sure all requirements are installed on your server or virtualenv that you're using on your server.
