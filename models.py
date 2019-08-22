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
