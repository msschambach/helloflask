from app.modules.blog import blog


def register_modules(app):
    app.register_blueprint(blog, url_prefix='/blog')
