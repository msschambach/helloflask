from flask import render_template as render


def handle_errors(app):

    @app.errorhandler(404)
    def not_found(error):
        return render('404.html', error=error), 404
