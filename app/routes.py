from flask import Flask, render_template, request, redirect, url_for, session 
from app.models import add_post,create_user, validate_user_login, get_all_posts, get_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app

app.secret_key = 'Testing123'

@app.route('/')
def index():
    try:
        current_user_id = session['user_id']
        user = get_user(current_user_id)
    except KeyError:
        user = None
    posts = get_all_posts()
   
    return render_template('index.html', posts = posts, user=user)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        create_user(username,password,email)

        return 'Register Successful'
    return render_template('register.html')



@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        user  = validate_user_login(username,password)
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        return "Invalid Information"
    
    return render_template('login.html')


@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('user_id', None)
    return redirect('login')


@app.route('/create-post', methods = ['GET','POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title'] 
        print(title)
        content = request.form['content'] 
        print(content)
        add_post(title, content, session['user_id'])
        return redirect(url_for('index'))
        
    return render_template('create_post.html')