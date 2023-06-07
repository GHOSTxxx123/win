import numpy as np
import io, base64
import os, secrets
from flask_login import login_required, logout_user, login_user, current_user
from flask import abort, json
from application import app, db
from application.models import Book, User, Message, Busy_Book
from flask import render_template, send_from_directory, request, flash, url_for, redirect, jsonify
from PIL import Image
from sqlalchemy.exc import IntegrityError

@app.route('/sign_in/', methods=('GET', 'POST'))
def sign_in():
    data = json.loads(request.data)
    username = data['username']
    password = data['password']
    user = db.session.query(User).filter(User.username == username).first()
    if user and user.password == password:
        return jsonify(user)
    else:
        data = {'user': False}

        return jsonify(data)

@app.route('/sign_up/')
def sign_up():
    data = json.loads(request.data)
    username = data['username']
    name = data['name']
    firstname = data['firstname']
    girdname = data['girdname']
    number = data['number']
    gmail = data['gmail']
    addres = data['addres']
    gryp = data['gryp']
    kyrs = data['kyrs']
    pol = data['pol']
    password = data['password']
    user = db.session.query(User).filter(User.username == username).first()
    user_number = db.session.query(User).filter(User.number == number).first()
    user_gmail = db.session.query(User).filter(User.gmail == gmail).first()
    if user:
        data = {'username': True}
        return jsonify(data)
    elif user_number:
        data = {'number': True}
        return jsonify(data)
    elif user_gmail:
        data = {'gmail': True}
        return jsonify(data)    
    else:
        gtoken = secrets.token_hex(15)
        user = User(
            username = username,
            name = name,
            firstname = firstname,
            girdname = girdname,
            number = number,
            gmail = gmail,
            addres = addres,
            gryp = gryp,
            kyrs = kyrs,
            pol = pol,
            password = password,
            token = gtoken
            )
        db.session.add(user)
        db.session.commit()
        data = {'sign_up': True}
        return  jsonify(data)

def save_pdf(bookpdf):
    bookpdf = io.BytesIO(base64.b64decode(bytes(str(bookpdf), "utf-8")))
    pdf_fn = secrets.token_hex(16) 
    pdf_path = os.path.join(app.root_path, app.config['UPLOAD_PDF'], f"{pdf_fn}.pdf")

    bookpdf.save(os.path.join(app.root_path, app.config['UPLOAD_PDF'], f"{pdf_fn}.pdf"))


    return f'{pdf_fn}.pdf'

def save_picture(cover):
    picture_fn = secrets.token_hex(16)
    picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")

    output_size = (220, 340)
    img = Image.open(io.BytesIO(base64.b64decode(bytes(str(cover), "utf-8"))))
    img.thumbnail(output_size)
    img.save(picture_path)
    img = np.array(img)


    return f"{picture_fn}.png"

@app.route('/create/', methods=('GET', 'POST'))
def create():
    data = json.loads(request.data)
    token = data['token']
    title = data['title']
    author = data['author']
    genre = data['genre']
    rating = data['rating']
    description = data['description']
    photo = data['photo']
    pdf = data['pdf']
    user = db.session.query(User).filter(User.token == token).first()
    if user and user.is_personal:
        if photo:
            cover = save_picture(photo)
        else:
            cover ='default.jpg'
        pdf_book = save_pdf(pdf)
        book = Book(title=title,
            author=author,
            genre=genre,
            rating=rating,
            cover=cover,
            bookpdf=pdf_book,
            description=description)
        db.session.add(book)
        db.session.commit()
        data = {'creat': True}
        return json(data)
    else:
        data = {'creat': False}
        return json(data)

@app.route('/book/')
def book():
    data = json.loads(request.data)
    token = data['token']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        data = Book.query.all()
        return jsonify(data)
    
@app.route('/message_save/')
def message_save():
    data = json.loads(request.data)
    token = data['token']
    body = data['body']
    msg_by = data['msg_by']
    msg_to = data['msg_to']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        message = Message(
            body=body,
            msg_by=msg_by,
            msg_to=msg_to)
        db.session.add(message)
        db.session.commit()

        data = {'save_message': True}

        return jsonify(data)
    

@app.route('/message/')
def message():
    data = json.loads(request.data)
    token = data['token']
    id = data['id']
    user_id = data['user_id']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        message_by_user = db.session.query(Message).filter(Message.msg_by == id).first()
        if message_by_user and message_by_user.msg_to == user_id:
            return jsonify(message_by_user)


@app.route('/busy_book/')
def busy_book():
    data = json.loads(request.data)
    token = data['token']
    user_id = data['user_id']
    book_id = data['book_id']
    title = data['title']
    busy_with = data['busy_with']
    busy_by = data['busy_by']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        bu = db.session.query(Busy_Book).filter(Busy_Book.title == title).first()
        if bu:
            data = {'book_busy': True}
        else:
            busy = Busy_Book(
                user_id=user_id,
                book_id=book_id,
                title=title,
                busy_with=busy_with,
                busy_by=busy_by
            )
            db.session.add(busy)
            busy_bo = Book.query.get_or_404(book_id)
            busy_bo.busy = True
            db.session.commit()
            data = {'book_busy_save': True}
            return jsonify(data)

@app.route('/uploads/cover/')
def send_file_cover():
    data = json.loads(request.data)
    token = data['token']
    filename = data['filename']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)    

@app.route('/uploads/pdf/')
def send_file_pdf():
    data = json.loads(request.data)
    token = data['token']
    filename = data['filename']
    user = db.session.query(User).filter(User.token == token).first()
    if user:
        return send_from_directory(app.config['UPLOAD_PDF'], filename)  

@app.post('/delete_book/')
@login_required
def delete(book_id):
    data = json.loads(request.data)
    token = data['token']
    book_id = data['book_id']
    user = db.session.query(User).filter(User.token == token).first()
    if user and user.is_personal:
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        data = {'book_del': True}
        return jsonify(data) 

@app.post('/delete_user/')
@login_required
def delete_user():
    data = json.loads(request.data)
    token = data['token']
    user_id = data['user_id']
    user = db.session.query(User).filter(User.token == token).first()
    if user and user.is_admin:
        book = User.query.get_or_404(user_id)
        db.session.delete(book)
        db.session.commit()
        data = {'user_del': True}
        return jsonify(data)
    

@app.route('/permision/')
def permision():
    data = json.loads(request.data)
    token = data['token']
    user_id = data['user_id']
    is_rol = data['is_rol']
    permis = data['permis']
    user = db.session.query(User).filter(User.token == token).first()
    if user and user.is_admin:
        if is_rol == 'is_personal':
            user = User.query.get_or_404(user_id)
            user.is_personal = True
            user.is_student = False
            user.is_admin = False
            db.session.commit()
        elif is_rol == 'is_student':
            user = User.query.get_or_404(user_id)
            user.is_personal = False
            user.is_student = True
            user.is_admin = False
            db.session.commit()
        elif is_rol == 'is_admin':
            user = User.query.get_or_404(user_id)
            user.is_personal = False
            user.is_student = False
            user.is_admin = True
            db.session.commit()



@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()