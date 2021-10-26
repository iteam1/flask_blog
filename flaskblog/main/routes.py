from flask import Blueprint
from flask import render_template, request, flash, url_for, redirect
from flaskblog.models import Post
from flasgger import swag_from
from flaskblog.main.forms import SearchForm

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
@swag_from('./docs/homePage.yml')
def home():
    # get all post
    # posts = Post.query.all()
    page = request.args.get('page',1,type = int) # find in path  page query, default value = 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page,per_page = 4) # paginate each page 4 posts
    form = SearchForm() # search form
    return render_template('home.html', posts = posts,form = form),200

@main.route("/about")
@swag_from('./docs/aboutPage.yml')
def about():
    return render_template('about.html', title = 'About'),201

@main.route("/search",methods = ['POST'])
@swag_from("./docs/search.yml")
def search_post():
    keyword = request.form.get('keyword')
    #flash(f'You just got a search {keyword}','info')
    result = [] # empty list contain result 
    posts = Post.query.all()
    for post in posts:
        if keyword.lower() in post.title.lower():
            result.append(post)

    total = len(result)
    
    return render_template('result.html', posts = result, title = 'Result', total = total),214

