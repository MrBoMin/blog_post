from flask import Flask 

app = Flask(__name__)
app.secrect_key = 'TestingKEY'

from app import routes