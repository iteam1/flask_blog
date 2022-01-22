![version](https://img.shields.io/badge/version-0.1-brightgreen) 
![priority](https://img.shields.io/badge/priority-normal-lightgrey) 
![kanban](https://img.shields.io/badge/status-done-yellowgreen)

# flask-blog

## home page

![Capture1](https://user-images.githubusercontent.com/73679364/138867626-324e4455-13d7-4d61-8837-aa0763263655.PNG)

## register

![Capture4](https://user-images.githubusercontent.com/73679364/138867966-bfa1af55-dbe8-4820-a5f9-09f613fcb73b.PNG)

## login

![Capture5](https://user-images.githubusercontent.com/73679364/138868039-de73f81c-73d7-4a8a-a758-c1eaf801eece.PNG)


![Capture6](https://user-images.githubusercontent.com/73679364/138868188-12c8db9f-bb04-41a4-ba20-5c578d1e2eff.PNG)

## logout

![Capture3](https://user-images.githubusercontent.com/73679364/138868246-5db24ca3-1bc2-4807-a961-622f066db7ce.PNG)

## account 

![Capture8](https://user-images.githubusercontent.com/73679364/138868546-8b2135e6-e5bf-4ea6-8e25-56157046deda.PNG)

![Capture9](https://user-images.githubusercontent.com/73679364/138868689-d9462b19-f2f7-4c00-b21d-9095a90aa544.PNG)


## create new post

![Capture2](https://user-images.githubusercontent.com/73679364/138867756-3ab64615-6824-43a8-a88e-1d274db91073.PNG)

## update & delete post

![Capture10](https://user-images.githubusercontent.com/73679364/138868821-99b5b38f-f913-4929-a882-d732da755f62.PNG)


![Capture11](https://user-images.githubusercontent.com/73679364/138868900-b775ce52-16e5-4c4f-8c83-133610f8b139.PNG)

## search tool

![Capture7](https://user-images.githubusercontent.com/73679364/138868439-75477e42-5375-4ca4-9891-0b4a58955504.PNG)

## pagination

![Capture12](https://user-images.githubusercontent.com/73679364/138869118-2b48d894-9437-4850-bad5-44d40a4c01be.PNG)

### api documents

![Capture13](https://user-images.githubusercontent.com/73679364/138869949-f1e7da7e-66d6-4cc3-b476-0357ceee89e3.PNG)

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
    
    Folder PATH listing for volume Disk
    Volume serial number is 324D-658E
    D:.
    |   flaskblog.py
    |   forms.py
    |   README.md
    |   requirements.txt
    |   site.db
    |   structure.txt
    |   
    +---docs
    |       aboutPage.yml
    |       homePage.yml
    |       register.yml
    |       
    +---static
    |       main.css
    |       
    +---templates
    |       about.html
    |       home.html
    |       layout.html
    |       login.html
    |       register.html
    |       
    \---__pycache__
            flaskblog.cpython-38.pyc
            forms.cpython-38.pyc
    
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

### 8/ CRUD Posts

### 9/ Pagination

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
      
 Pagition by oder
 
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page,per_page = 4)
    
 ### 10/ Email and password reset
 
   ![Capture](https://user-images.githubusercontent.com/73679364/138622404-0c038e36-c10a-4785-b7ed-9262ac0f7bc1.PNG)
   
    pip install flask-mail

### 11/ blueprint

    Folder PATH listing for volume Disk
    Volume serial number is 324D-658E
    D:.
    |   README.md
    |   requirements.txt
    |   run.py
    |   structure.txt
    |   
    +---flaskblog
    |   |   config.py
    |   |   models.py
    |   |   site.db
    |   |   __init__.py
    |   |   
    |   +---main
    |   |   |   forms.py
    |   |   |   routes.py
    |   |   |   __init__.py
    |   |   |   
    |   |   +---docs
    |   |   |       aboutPage.yml
    |   |   |       homePage.yml
    |   |   |       
    |   |   \---__pycache__
    |   |           routes.cpython-38.pyc
    |   |           __init__.cpython-38.pyc
    |   |           
    |   +---posts
    |   |   |   forms.py
    |   |   |   routes.py
    |   |   |   __init__.py
    |   |   |   
    |   |   +---docs
    |   |   |       postDelete.yml
    |   |   |       postID.yml
    |   |   |       postsNew.yml
    |   |   |       postUpdate.yml
    |   |   |       
    |   |   \---__pycache__
    |   |           forms.cpython-38.pyc
    |   |           routes.cpython-38.pyc
    |   |           __init__.cpython-38.pyc
    |   |           
    |   +---static
    |   |   |   main.css
    |   |   |   
    |   |   \---profile_pics
    |   |           02cf61d77a003a6a.png
    |   |           117596b3e34acfab.jpg
    |   |           249681dc57704068.png
    |   |           dad3c0f7b846c32d.png
    |   |           default.jpg
    |   |           
    |   +---templates
    |   |   |   about.html
    |   |   |   account.html
    |   |   |   create_post.html
    |   |   |   home.html
    |   |   |   layout.html
    |   |   |   login.html
    |   |   |   post.html
    |   |   |   register.html
    |   |   |   reset_password.html
    |   |   |   reset_request.html
    |   |   |   user_posts.html
    |   |   |   
    |   |   \---includes
    |   |           delete_modal.html
    |   |           
    |   +---users
    |   |   |   forms.py
    |   |   |   routes.py
    |   |   |   utils.py
    |   |   |   __init__.py
    |   |   |   
    |   |   +---docs
    |   |   |       account.yml
    |   |   |       loginGet.yml
    |   |   |       loginPost.yml
    |   |   |       logout.yml
    |   |   |       registerGet.yml
    |   |   |       registerPost.yml
    |   |   |       resetPassword.yml
    |   |   |       resetRequest.yml
    |   |   |       userPost.yml
    |   |   |       
    |   |   \---__pycache__
    |   |           forms.cpython-38.pyc
    |   |           routes.cpython-38.pyc
    |   |           utils.cpython-38.pyc
    |   |           __init__.cpython-38.pyc
    |   |           
    |   \---__pycache__
    |           config.cpython-38.pyc
    |           forms.cpython-38.pyc
    |           models.cpython-38.pyc
    |           routes.cpython-38.pyc
    |           __init__.cpython-38.pyc
    |           
    +---snippets
    |       blueprint_imports.txt
    |       
    \---__pycache__
            flaskblog.cpython-38.pyc
            forms.cpython-38.pyc

### 12/ Error Handle

### 13/ SearchBar

### 14/ Deploy on heroku

https://devcenter.heroku.com/articles/heroku-cli

    $ heroku login
    
    Ctrl + C
    
    heroku create
    
    https://evening-earth-87743.herokuapp.com/
    
    heroku rename flaskblogfornewone
    
    heroku open
    
    git push heroku main

https://www.youtube.com/watch?v=6DI_7Zja8Zc

### 15/ Custom domain

https://www.youtube.com/watch?v=LUFn-QVcmB8&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=14

### 16/ How to enable HTTPS with a free SSL/TLS Certificate using Let's Encrypt

https://www.youtube.com/watch?v=Gdys9qPjuKs&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=16

## refer to
### youtube
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### github
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog

