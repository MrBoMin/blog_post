import psycopg2 
from psycopg2 import sql 

def get_db():
    conn = psycopg2.connect(
        dbname = "blog_post",
        user='postgres',
        password='felix', 
        host='localhost', 
        port = '5432'
    )

    return conn