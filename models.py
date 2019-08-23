"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """ Connect to database  """
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User people"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)

    last_name = db.Column(db.String(50),
                          nullable=False)

    image_url = db.Column(db.String(250))


class Post(db.Model):
    """Post that users post haha"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.String(55),
                      nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime,
                           nullable=False)
    creator_id = db.Column(db.Integer,
                           db.ForeignKey('users.id'))
    creator = db.relationship('User', backref="posts")
    post_tag = db.relationship('PostTag',backref="posts")

class Tag(db.Model):
    """ Tag id and name """

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(45),
                     unique=True,
                     nullable=False)
    post_tag = db.relationship('PostTag', backref="tags")
    posts = db.relationship('Post',
                            secondary="posts_tags",
                            backref="tags")


class PostTag(db.Model):
    """ Mapping posts to a tag"""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey("posts.id"),
                        primary_key=True)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey("tags.id"),
                       primary_key=True)
                        