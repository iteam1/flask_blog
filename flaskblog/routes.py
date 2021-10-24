from flask import render_template,flash, redirect,url_for,request,abort
from flaskblog import app,db,bcrypt 
from flaskblog.forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm
from flaskblog.models import User,Post
from flasgger import Swagger,swag_from
from flask_login import login_user,current_user,logout_user,login_required
import secrets # for generate new name of the picture upload
import os # for generate new name of the picture upload
from PIL import Image # for generate new name of the picture upload

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
    #Get all post
    posts = Post.query.all()
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

# this function for generate new name of the upload picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name,f_ext = os.path.splitext(form_picture.filename) # split the extesion out the picture name
    picture_fn = random_hex + f_ext # picture new name 
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn) # create a path

    output_size = (125,125) # follow css style
    i = Image.open(form_picture) # create a new image follow css style
    i.thumbnail(output_size)

    i.save(picture_path) # save the new picture into picture path
    return picture_fn 

@app.route("/account",methods = ['GET','POST'])
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
        return redirect(url_for('account'))
    # if there is a get request, display current_user's info on the form
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html',title = 'Account',image_file = image_file,form = form),206

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
@swag_from('./docs/postsNew.yml')
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # create a post object
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        # add new record into database table
        db.session.add(post)
        db.session.commit()
        flash(f'Your post has been created','success')
        return redirect(url_for('home')) 
    return render_template('create_post.html',title = 'New Post',form = form, legend = 'New Post'),207

@app.route("/post/<int:post_id>")
@swag_from("./docs/postID.yml")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if post:
        return render_template('post.html',title = post.title, post =post),208

@app.route("/post/<int:post_id>/update",methods = ['GET','POST'])
@login_required 
@swag_from('./docs/postUpdate.yml')
def update_post(post_id):
    # get the post 
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    # if you press submit, update your post
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Your post have been update!','success')
        return redirect(url_for('post',post_id=post.id)) # return to this post's page
    
    elif request.method == 'GET':
        # display content in the form
        form.title.data = post.title # display title inside form's title 
        form.content.data = post.content # displat content inside form's content

    return render_template('create_post.html',title = 'Update Post', form = form, legend = 'Update Post'),209

@app.route("/post/<int:post_id>/delete",methods = ['POST'])
@login_required
@swag_from('./docs/postDelete.yml') 
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post have been deleted!','success')
    return redirect(url_for('home'))

