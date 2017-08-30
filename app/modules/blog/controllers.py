from flask import render_template as render

from app.modules.blog import blog


@blog.route('/')
def blog_index():
    return render('index.html')


@blog.route('/posts')
def blog_posts():
    return render('posts.html')
