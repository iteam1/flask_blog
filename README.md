# flask-blog

## content

### 1/ App and swagger ui

    pip install flask
    pip install flasgger
    
Apidocs link

    http://127.0.0.1:5000/apidocs/

### 2/ Template

### 3/ Form and User input

    pip install flask_wtf
    pip install email_validator

### 4/ Database

    pip install flask_sqlalchemy

Create database
    
    db.create_all()
    
Add new row into database 

    db.session.add(user_1)
    db.session.commit()
    
Query in 'user' table

    User.query.all()
    User.query.filter_by(username = 'Corey')
    User.query.filter_by(username = 'Corey').first()
    User.query.filter_by(username = 'Corey').all()
    User.query.get(1)

Delete all table

    db.drop_all()
    
### 5/ Package Structure

Cmd command

    tree /a /f > stucture.txt 
  
Structure

    Volume serial number is 324D-658E
    D:.
    |   README.md
    |   requirements.txt
    |   run.py
    |   sturcture.txt
    |   
    +---flaskblog
    |   |   forms.py
    |   |   models.py
    |   |   routes.py
    |   |   site.db
    |   |   __init__.py
    |   |   
    |   +---docs
    |   |       aboutPage.yml
    |   |       homePage.yml
    |   |       loginGet.yml
    |   |       loginPost.yml
    |   |       registerGet.yml
    |   |       registerPost.yml
    |   |       
    |   +---static
    |   |       main.css
    |   |       
    |   +---templates
    |   |       about.html
    |   |       home.html
    |   |       layout.html
    |   |       login.html
    |   |       register.html
    |   |       
    |   \---__pycache__
    |           forms.cpython-38.pyc
    |           models.cpython-38.pyc
    |           routes.cpython-38.pyc
    |           __init__.cpython-38.pyc
    |           
    \---__pycache__
            flaskblog.cpython-38.pyc
            forms.cpython-38.pyc
        
### 6/ User Authentication

    pip install flask-bcrypt
    pip install flask-login

Go to the next page after login:

    http://127.0.0.1:5000/login?next=%2Faccount
    
### 7/ Account's profile update
    
Resize the avatar image

    pip install pillow

### 8/CRUD Posts

### 9/Pagination

Query posts by pagination

    posts = Post.query.paginate()

Show the elements in posts object

    dir(posts)

Show post in posts object

    posts.items

Current page in posts object created by pagination

    posts.page
    
The page number in each page    
    
    posts.per_page
    
Show the posts in page 2 
    
    posts = Post.query.paginate(page = 2)
    
Show the posts in first page with 4 posts each page

    posts = Post.query.paginate(per_page = 4)
    
Total post

    posts.total
    
Show the iteration of page you can access at your current page
    
    posts = Post.query.paginate(page = 2)
    
    for iter in posts.iter_pages:
      print(iter)
      
## refer to
### youtube
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### github
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
