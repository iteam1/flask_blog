from flask import render_template,flash, redirect,url_for,request
from flaskblog import app,db,bcrypt 
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post
from flasgger import Swagger,swag_from
from flask_login import login_user,current_user,logout_user,login_required

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
    #Check if user is already login
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm() # send form to register page
        if form.validate_on_submit(): # if receive a form and it valid
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #decode password into a string, not a bytes 
            user = User(username=form.username.data,email=form.email.data,password = hashed_password) # create a user
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!, You are now able to login','success') # show a one time message with caterory = success
            return redirect(url_for('login'))
        return render_template('register.html',title= 'Register',form = form),202

@app.route("/login", methods = ['GET','POST'])
@swag_from('./docs/loginGet.yml',methods = ['GET'])
@swag_from('./docs/loginPost.yml',methods = ['POST'])
def login():
    #Check if user is already login
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first() # Check the user exist
            if user and bcrypt.check_password_hash(user.password,form.password.data): # Check the password
                login_user(user,remember = form.remember.data)
                flash(f'Login Successed, Wellcome {user.username}!','success')
                # go to the next page if requestion exist ex: http://127.0.0.1:5000/login?next=%2Faccount
                next_page = request.args.get('next') # return none if next argument exist
                return redirect(next_page) if next_page else redirect(url_for('home')) # return conditional
            else:
                flash(f'Login Failed, Please check email and password','danger')

        return render_template('login.html',title = 'Login', form = form),203

@app.route("/logout")
@swag_from('./docs/logout.yml')
def logout():
    logout_user()
    flash(f'You are logout!','info')
    return redirect(url_for('home'))

@app.route("/account")
@login_required # need login to access this route
@swag_from('./docs/account.yml')
def account():
    return render_template('account.html',title = 'Account'),206

