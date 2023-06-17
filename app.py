from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = 'gK_!CZy=}E8,MM'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(200))
    tasks = db.relationship('Task', lazy = True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

