from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET'])
def users():
    if request.method=='POST':
        nombre = request.form.get('username')
        email = request.form.get('email')
        nuevo_usuario = User(username=username, email=email)
        db.session.add(nuevo_usuario)
    usuarios=User.query.all()
    return render_template('users.html', users=[])

if __name__ == '__main__':
    app.run(debug=True)
