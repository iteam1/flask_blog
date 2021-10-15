from flask import Flask
from flasgger import Swagger,swag_from

app = Flask(__name__)

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
    return "<h1>Home Page!</h1>",200

@app.route("/about")
@swag_from('./docs/aboutPage.yml')
def about():
    return "<h1>About Page</h1>",201

if __name__ == "__main__":
    app.run(debug = True)