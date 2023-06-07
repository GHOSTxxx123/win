from application import app, db
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
    busy: bool 
    created_at: str
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    bookpdf = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    busy = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Book {self.title}>'
        
@dataclass
class Busy_Book(db.Model):
    id: int
    user_id: int
    book_id: int
    title: str
    took: bool
    busy_with: str
    busy_by: str

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    title = db.Column(db.String(100), unique=True, nullable=False)
    took = db.Column(db.Boolean, default=False)
    busy_with = db.Column(db.DateTime(), nullable=False)
    busy_by = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'<Busy_Book {self.id}>'
    

@dataclass
class Stolo_Golos(db.Model):
    id: int 
    user_id: int
    title: str
    data: str

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(20), nullable=False)
    data = db.Column(db.DateTime(), default=datetime.utcnow)


@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id: int
    username: str
    name: str
    firstname: str
    girdname: str
    number: int
    gmail: str
    addres: str
    gryp: str
    kyrs: int
    pol: str
    password: str
    token: str
    is_student: bool
    is_personal: bool
    is_admin: bool
    created_on: str
    updated_on: str
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    girdname = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    gmail = db.Column(db.String(100), unique=True, nullable=False)
    addres = db.Column(db.String(100), nullable=False)
    gryp = db.Column(db.String(7), nullable=False)
    kyrs = db.Column(db.Integer)
    pol = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    is_student = db.Column(db.Boolean, default=True)
    is_personal = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,  onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

@dataclass
class Message(db.Model):
    __tablename__ = 'message'
    id: int
    body: str
    msg_by: str
    msg_to: str
    msg_time: int
    read: bool

    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
    msg_by = db.Column(db.String(100), nullable=False)
    msg_to = db.Column(db.String(100), nullable=False)
    msg_time = db.Column(db.DateTime(), default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f'<Message {self.body}>'


    
