from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    profile_picture = db.Column(db.String(2000))
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15))
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }   

class UserFollower(db.Model):
    __tablename__ = 'user_followers'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class UserFollowing(db.Model):
    __tablename__ = 'user_following'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image = db.Column(db.String(2000), nullable=False)
    caption = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, image: str, user_id: int):
        self.image = image
        self.user_id = user_id
        
    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }

class PostLike(db.Model):
    __tablename__ = 'post_likes'
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class CommentLike(db.Model):
    __tablename__ = 'comment_likes'
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
