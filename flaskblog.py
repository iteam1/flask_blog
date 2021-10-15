from flask import Flask,render_template
from flasgger import Swagger,swag_from

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug = True)