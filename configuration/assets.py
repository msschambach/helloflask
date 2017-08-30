import os
from flask_assets import Environment, Bundle
from webassets.filter import get_filter
from configuration import BASE_DIR


def create_assets(app):
    assets = Environment(app)

    scss = get_filter('scss', as_output=True)
    scss.load_paths = [
        os.path.join(BASE_DIR, 'app/modules/blog/static/sass')
    ]
    cssmin = get_filter('cssmin')
    jsmin = get_filter('jsmin')

    assets.register(
        'blog_styles',
        Bundle(
            'blog/sass/main.scss',
            filters=(scss, cssmin), output='css/blog.min.css'
        )
    )

    assets.register(
        'blog_scripts',
        Bundle(
            'blog/js/main.js',
            filters=jsmin, output='js/blog.min.js'
        )
    )

    return assets
