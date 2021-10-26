import os
import secrets
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from flaskblog import mail

# this function for generate new name of the upload picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name,f_ext = os.path.splitext(form_picture.filename) # split the extesion out the picture name
    picture_fn = random_hex + f_ext # picture new name 
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn) # create a path

    output_size = (125,125) # follow css style
    i = Image.open(form_picture) # create a new image follow css style
    i.thumbnail(output_size)

    i.save(picture_path) # save the new picture into picture path
    return picture_fn 

# create a function for send a email to reset password
# _external = True using absolute url
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',sender = 'noreply@demo.com',
                                            recipients = [user.email] )
    msg.body = f''' To reset your password, visit the following link:
{ url_for('reset_password',token = token,_external = True) }
If you did not make this request, then simply ignore this email and no changes will be made
'''