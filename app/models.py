from app.db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username,password,email):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute('INSERT INTO users(username,password,email) VALUES (%s,%s,%s)', (username,password,email))
        db.commit() 


def validate_user_login(username,password):
    db = get_db() 
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[2], password):
            return user
        
    return None



def get_all_posts():
    db = get_db() 
    with db.cursor() as cursor: 
        cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
        posts = cursor.fetchall() 
    return posts