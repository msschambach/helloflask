from app import app
from celery import Celery

celeryapp = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                   broker=app.config['CELERY_BROKER_URL'])

celeryapp.conf.update(app.config)
BaseTask = celeryapp.Task

class ContextTask(BaseTask):
    abstract = True

    def __call__(self, *args, **kwargs):
        with app.app_context():
            return BaseTask.__call__(self, *args, **kwargs)


celeryapp.Task = ContextTask
