from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email
from flasgger import swag_from

users = Blueprint('users',__name__)

@users.route("/register",methods = ['GET','POST'])
@swag_from('./docs/registerGet.yml',methods = ['GET'])
@swag_from('./docs/registerPost.yml',methods = ['POST'])
def register():
    # check if user is already login
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = RegistrationForm() # send form to register page
        if form.validate_on_submit(): # if receive a form and it valid
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # decode password into a string, not a bytes 
            user = User(username=form.username.data,email=form.email.data,password = hashed_password) # create a user
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!, You are now able to login','success') # show a one time message with caterory = success
            return redirect(url_for('users.login'))
        return render_template('register.html',title= 'Register',form = form),202

@users.route("/login", methods = ['GET','POST'])
@swag_from('./docs/loginGet.yml',methods = ['GET'])
@swag_from('./docs/loginPost.yml',methods = ['POST'])
def login():
    #Check if user is already login
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first() # Check the user exist
            if user and bcrypt.check_password_hash(user.password,form.password.data): # Check the password
                login_user(user,remember = form.remember.data)
                flash(f'Login Successed, Wellcome {user.username}!','success')
                # go to the next page if requestion exist ex: http://127.0.0.1:5000/login?next=%2Faccount
                next_page = request.args.get('next') # return none if next argument exist
                return redirect(next_page) if next_page else redirect(url_for('main.home')) # return conditional
            else:
                flash(f'Login Failed, Please check email and password','danger')

        return render_template('login.html',title = 'Login', form = form),203

@users.route("/logout")
@swag_from('./docs/logout.yml')
def logout():
    logout_user()
    flash(f'You are logout!','info')
    return redirect(url_for('main.home'))

@users.route("/account",methods = ['GET','POST'])
@login_required # need login to access this route
@swag_from('./docs/account.yml')
def account():
    form = UpdateAccountForm()
    # if there is a post request
    if form.validate_on_submit():
        if form.picture.data: # if there is a picture in update file
            picture_file = save_picture(form.picture.data) # save the new name
            current_user.image_file = picture_file # update current user ' new picture name
        current_user.username = form.username.data # current_user use class User
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your account has been updated','success')
        return redirect(url_for('users.account'))
    # if there is a get request, display current_user's info on the form
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html',title = 'Account',image_file = image_file,form = form),206

# all account's posts
@users.route("/user/<string:username>")
@swag_from('./docs/userPost.yml')
def user_post(username):
    page = request.args.get('page',1,type = int) # find in path  page query, default value = 1
    user = User.query.filter_by(username = username).first_or_404() # find ther user base on username, if not return Fasle
    posts = Post.query.filter_by(author = user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page = page,per_page = 4)
    return render_template('user_posts.html', posts = posts,user = user),211

# this route is send request for reset password 
@users.route("/reset_password",methods = ['GET','POST'])
@swag_from('./docs/resetRequest.yml')
def reset_request():
    if current_user.is_authenticated: # make sure the user is logout before reset password
        flash(f'Please logout before reset your password!','info')
        return redirect(url_for('main.home'))
    form =RequestResetForm()
    if form.validate_on_submit(): # if received a form
        user = User.query.filter_by(email= form.email.data).first()
        if user:
            send_reset_email(user)
            flash(f'An email has been sent with instructions to reset your password to you, It will expire after 30 minutes','info') 
            return redirect(url_for('users.login'))
        else:
            flash(f'There is no user use this email, please check your email again','info')

    return render_template('reset_request.html',title = 'Reset Password', form = form),212

# go to this route by the link in the email
@users.route("/reset_password/<token>",methods = ['GET','POST'])
@swag_from("./docs/resetPassword.yml")
def reset_password(token):
    if current_user.is_authenticated:
        flash(f'Please logout before reset your password!','info')
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token) # verify the token, return the user 
    if user is None: # if not user
        flash(f'That is invalid or expired token','warning','info')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('reset_password.html',title = 'Reset Password',form = form)