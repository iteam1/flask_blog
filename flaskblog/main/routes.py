from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flasgger import swag_from

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
@swag_from('./docs/homePage.yml')
def home():
    # get all post
    # posts = Post.query.all()
    page = request.args.get('page',1,type = int) # find in path  page query, default value = 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page,per_page = 4) # paginate each page 4 posts
    return render_template('home.html', posts = posts),200

@main.route("/about")
@swag_from('./docs/aboutPage.yml')
def about():
    return render_template('about.html', title = 'About'),201

