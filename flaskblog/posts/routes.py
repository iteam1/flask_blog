from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from flasgger import swag_from

posts = Blueprint('posts',__name__)

@posts.route("/post/new", methods=['GET', 'POST'])
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
        return redirect(url_for('main.home')) 
    return render_template('create_post.html',title = 'New Post',form = form, legend = 'New Post'),207

@posts.route("/post/<int:post_id>")
@swag_from("./docs/postID.yml")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if post:
        return render_template('post.html',title = post.title, post =post),208

@posts.route("/post/<int:post_id>/update",methods = ['GET','POST'])
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
        return redirect(url_for('posts.post',post_id=post.id)) # return to this post's page
    
    elif request.method == 'GET':
        # display content in the form
        form.title.data = post.title # display title inside form's title 
        form.content.data = post.content # displat content inside form's content

    return render_template('create_post.html',title = 'Update Post', form = form, legend = 'Update Post'),209

@posts.route("/post/<int:post_id>/delete",methods = ['POST'])
@login_required
@swag_from('./docs/postDelete.yml') 
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post have been deleted!','success')
    return redirect(url_for('main.home'))