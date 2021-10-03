from flask import Flask
from flasgger import Swagger  

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug = True)