from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

#to run vm =   "C:\Users\zgiba\Desktop\to-do\myenv\Scripts\Activate.ps1"

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

    def __init__(self,username,email, password):
        self.username = username
        self.email = email
        self.password = password


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.route('/',methods=['GET'])
def main_page():
    return render_template('main.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        if password = confirm_password:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            return redirect('/login')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

