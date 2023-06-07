from reader import app, db
from sqlalchemy.sql import func
from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin 

@dataclass
class Book(db.Model):
    id: int
    title: str
    author: str
    genre: str
    cover: str
    bookpdf: str
    rating: int
    description: str
    notes: str
    created_at: str
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    bookpdf = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Book {self.title}>'
        

@app.login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

@dataclass
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: int
    name: str
    firstname: str
    gmail: str
    readbilet: int
    pass_hash: str
    kyrs: int
    created_on: str
    updated_on: str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    gmail = db.Column(db.String(20), nullable=False)
    readbilet = db.Column(db.Integer, unique=True, nullable=False)
    pass_hash = db.Column(db.String(100), nullable=False)
    kyrs = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,  onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'