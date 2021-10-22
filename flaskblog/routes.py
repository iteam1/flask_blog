from flask import render_template,flash, redirect,url_for
from flaskblog import app 
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post
from flasgger import Swagger,swag_from

posts = [
    {
        "author": 'Loc Chuong',
        "title": 'Blog Post 1',
        "content": 'First post content',
        "date_posted": 'April 21, 2018' 
    },
    {
        "author": 'Loc Chuong',
        "title": 'Blog Post 2',
        "content": 'Second post content',
        "date_posted": 'April 21, 2018' 
    }

]

#define a template Info Object
template = {
    "swagger":"2.0",
    "info":{
        "title":"FlaskBlog Backend",
        "description":"FlaskBlog API documments",
        "contact":{
            "name": "LocChuong",
            "url": "http://www.swagger.io/support",
            "email": "locchuong123@gmail.com"
        },
        "version":"0.0.1",
        "schemes":['http','https']
    }
}
swagger = Swagger(app,template = template)

@app.route("/")
@app.route("/home")
@swag_from('./docs/homePage.yml')
def home():
    return render_template('home.html', posts = posts),200

@app.route("/about")
@swag_from('./docs/aboutPage.yml')
def about():
    return render_template('about.html', title = 'About'),201

@app.route("/register",methods = ['GET','POST'])
@swag_from('./docs/registerGet.yml',methods = ['GET'])
@swag_from('./docs/registerPost.yml',methods = ['POST'])
def register():
    form = RegistrationForm() # send form to register page
    if form.validate_on_submit(): # if receive a form and it valid
        flash(f'Account created for {form.username.data}!','success') # show a one time message with caterory = success
        return redirect(url_for('home'))
    return render_template('register.html',title= 'Register',form = form),202

@app.route("/login", methods = ['GET','POST'])
@swag_from('./docs/loginGet.yml',methods = ['GET'])
@swag_from('./docs/loginPost.yml',methods = ['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed, Please check email and password','danger')


    return render_template('login.html',title = 'Login', form = form),203