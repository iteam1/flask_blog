# flask-blog

## content

### 1/ App and swagger ui

    pip install flask
    pip install flasgger

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
    
### 5/ Package Structure
### 6/ User Authentication

## refer to
### youtube
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### github
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
