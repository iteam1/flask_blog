from flask import Flask,render_template,flash, redirect,url_for
from flasgger import Swagger,swag_from
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a745e902cf3b161c90630fc2ae745351'

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
@swag_from('./docs/register.yml')
def register():
    form = RegistrationForm() # send form to register page
    if form.validate_on_submit(): # if receive a form and it valid
        flash(f'Account created for {form.username.data}!','success') # show a one time message with caterory = success
        return redirect(url_for('home'))
    return render_template('register.html',title= 'Register',form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed, Please check email and password','danger')


    return render_template('login.html',title = 'Login', form = form),202
if __name__ == "__main__":
    app.run(debug = True)