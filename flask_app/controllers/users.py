from flask import render_template, redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/login_page')

@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/create_user', methods = ['POST'])
def create_user():

    if not User.validate(request.form):
        return redirect('/')

    user = User.create_user(request.form)
    return redirect('/')

@app.route('/show_user/<int:id>')
def show_user(id):
    user = User.get_user(id)
    return render_template("show_user.html", user=user)

