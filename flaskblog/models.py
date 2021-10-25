from datetime import datetime
from flaskblog import db, login_manager,app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer # extension lib for generate token to reset account

# create a function to get the user by the id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class 'User' create a table's name lowercase 'user'
class User(db.Model,UserMixin): 
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique = True,nullable = False)
    email = db.Column(db.String(120),unique = True,nullable = False)
    image_file = db.Column(db.String(20),nullable = False,default = 'default.jpg')
    password = db.Column(db.String(60),nullable = True)
    posts = db.relationship('Post',backref ='author',lazy = True)

    def get_reset_token(self,expires_sec = 1800): # create a function for generate token for reset password
        s = Serializer(app.config['SECRET_KEY'],expires_sec) # create a object generate token follow your app's secret key
        return s.dumps({'user_id':self.id}).decode('utf-8') # return the token follow user id

    @staticmethod # decorate this function is a static method (not expect self parameter as an argument,accept token as argument)
    def verify_reset_token(token): # this function for verify the token received from the email
        s = Serializer(app.config['SECRET_KEY']) # create a object generate token follow your app's secret key without time expires
        try: # decode the user's id to get the token
            user_id = s.loads(token)['user_id'] # ex: {'user_id':1}
        except:
            return None 
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    content = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False) # reference to the 'user' table

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
