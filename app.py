"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, url_for
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from datetime import datetime

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
    posts = Post.query.filter(Post.creator_id == id).all()
    return render_template('userdetail.html', user=userp, posts=posts)

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

@app.route("/users/<int:id>/posts/new")
def show_form_post(id):
    """ Show the form so the user can input data """

    return render_template("createpost.html", id=id)


@app.route("/users/<int:id>/posts/new", methods=["POST"])
def create_post(id):
    """ verifies and adds post to database """
    title = request.form.get("title")
    content = request.form.get("content")
    posttime = datetime.now()
    post = Post(title=title, content=content, created_at=posttime, creator_id=id)
    # raise
    db.session.add(post)
    db.session.commit()

    return redirect(url_for("user_page", id=id))


@app.route("/posts/<int:id>")
def show_post(id):
    """ Show the post """
    post = (db.session.query(Post.title,
                             Post.id,
                             Post.content, User.id,
                             User.first_name,
                             User.last_name)
            .join(User).filter(Post.id == id))
    # post = postall.filter(Post.id == id)
    # raise
    return render_template("post.html", post=post)
