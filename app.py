"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'lalalaalala'
#toolbar = DebugToolbarExtension(app)


connect_db(app)


@app.route("/")
def redirect_users():
    """redirects to users list page """

    return redirect("/users")


@app.route("/users")
def list_user():
    """ List users and give option to create user """

    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users/new")
def create_new_user_form():
    """form page for creating new user"""

    return render_template('createuser.html')


@app.route("/users/new", methods=["POST"])
def create_new_redirect():
    """redirect page after creating new user"""
    firstname = request.form.get("first-name")
    lastname = request.form.get("last-name")
    imgurl = request.form.get("img-url")
    # print("this is one of our requests", firstname)
    if firstname == "":
        flash("Must include first name")
        return redirect('/users/new')
    if lastname == "":
        flash("Must include last name")
        return redirect('/users/new')
    

    rand = User(first_name=firstname, last_name=lastname, image_url=imgurl)
    db.session.add(rand)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:id>')
def user_page(id):
    userp = User.query.get(id)
    return render_template('userdetail.html', user=userp)

@app.route("/users/<int:id>/edit")
def edit_user_form(id):
    """form page for editing user"""

    return render_template('edituser.html', id=id)


@app.route("/users/<int:id>/edit", methods=["POST"])
def edit_user_redirect(id):
    """redirect page after editing user"""
    user = User.query.get_or_404(id)
    firstname = request.form.get("first-name")
    lastname = request.form.get("last-name")
    imgurl = request.form.get("img-url")
    print("last name", lastname)
    
    if firstname != "":
        user.first_name = firstname
    if lastname != "":
        user.last_name = lastname
    if imgurl != "":
        user.image_url = imgurl

    db.session.add(user)
    db.session.commit()
    return redirect('/users')


@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user_redirect(id):
    """redirect page after deleting user"""    
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
