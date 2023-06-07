import os, secrets
from flask_login import login_required, logout_user, login_user, current_user
from flask import abort
from reader import app, db
from reader.models import Book, User
from flask import render_template, send_from_directory, request, flash, url_for, redirect, jsonify
#from werkzeug.security import generate_password_hash,  check_password_hash
from PIL import Image
from reader.forms import BookForm, UpdateBook, Sign_in, Sign_up
from sqlalchemy.exc import IntegrityError



@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sign_in'))

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/sign_in/', methods=('GET', 'POST'))
def sign_in():
    form = Sign_in()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.readbilet == form.name.data).first()
        #password = db.session.query(User).filter(User.pass_hash == form.password.data).first()
        if user and user.pass_hash == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))

    return render_template('sign_in.html', form=form)

@app.route("/sign_in/<string:name>/<string:password>/")
def api_sign_in(name, password):
    user = db.session.query(User).filter(User.readbilet == name).first()
    if user and user.pass_hash == password:
        data = {'sign_in': True}
        return jsonify(data)
    else:
        data = {'sign_in': False}
        return jsonify(data)


@app.route('/sign_up/', methods=['POST', 'GET'])
def sign_up():
    form = Sign_up()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    firstname=form.firstname.data,
                    gmail=form.gmail.data,
                    readbilet=form.readbilet.data,
                    pass_hash=form.password.data,
                    kyrs=form.kyrs.data)
        db.session.add(user)
        db.session.commit()        
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', form=form)

@app.route("/sign_up/<string:name>/<string:firstname>/<string:gmail>/<string:read>/<string:passw>/<int:kyrs>")
def api_sign_up(name, firstname, gmail, read, passw, kyrs):
    readbilet = db.session.query(User).filter(User.readbilet == read).first()
    if readbilet:
        data = {'sign_up': 'Номер читательского билета уже используется     '}
        return jsonify(data)
    elif not readbilet:
        user = User(name=name,
                    firstname=firstname,
                    gmail=gmail,
                    readbilet=read,
                    pass_hash=passw,
                    kyrs=kyrs)
        db.session.add(user)
        db.session.commit()
        data = {'sign_up': True}
        return jsonify(data)



@app.route('/')
@login_required
def index():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.order_by(Book.created_at.desc()).paginate(page=page, per_page=4)
        return render_template('index.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.order_by(Book.created_at.desc()).paginate(page=page, per_page=4)
        return render_template('sindex.html', books=books)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    

@app.route('/<int:book_id>/')
@login_required
def book(book_id):
    if current_user.is_admin:
        book = Book.query.get_or_404(book_id)
        return render_template('book.html', book=book)
    elif not current_user.is_admin:
        return abort(404)      

@app.route('/thrillers/')
@login_required
def thrillers():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'триллер').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'триллер').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)

@app.route('/drama/')
@login_required
def drama():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'драма').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'драма').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)

@app.route('/fantastic/')
@login_required
def fantastic():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'фэнтези').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'фэнтези').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)


@app.route('/detectiv/')
@login_required
def detectiv():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'детектив').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'детектив').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)

@app.route('/biografi/')
@login_required
def biografi():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'биографии').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'биографии').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)

@app.route('/programing/')
@login_required
def programing():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'программирование').paginate(page=page, per_page=4)
        return render_template('thrillers.html', books=books)
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.genre == 'программирование').paginate(page=page, per_page=4)
        return render_template('sthrillers.html', books=books)


@app.route('/best/')
@login_required
def best():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.rating > 4).paginate(page=page, per_page=4)
        return render_template('best.html', books=books)      
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.rating > 4).paginate(page=page, per_page=4)
        return render_template('sbest.html', books=books)

@app.route('/search/', methods=['POST', 'GET'])
@login_required
def search():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.rating > 1).paginate(page=page, per_page=4)
        return render_template('search.html', books=books)      
    elif not current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.rating > 1).paginate(page=page, per_page=4)
        return render_template('ssearch.html', books=books)

def save_picture(cover):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(cover.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], picture_fn)

    output_size = (220, 340)
    i = Image.open(cover)
    i.thumbnail(output_size)
    i.save(picture_path)

    

    return picture_fn

def save_pdf(bookpdf):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(bookpdf.filename)
    pdf_fn = random_hex + f_ext
    pdf_path = os.path.join(app.root_path, app.config['UPLOAD_PDF'], pdf_fn)

    print(f"{pdf_path}, {pdf_fn}")
    bookpdf.save(os.path.join(app.root_path, app.config['UPLOAD_PDF'], pdf_fn))


    return pdf_fn

@app.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    if current_user.is_admin:
        form = BookForm()
        if form.validate_on_submit():
            if form.cover.data:
                cover = save_picture(form.cover.data)
            else:
                cover ='default.jpg'
            pdf_book = save_pdf(form.bookpdf.data)   
            title = form.title.data
            author = form.author.data
            genre = form.genre.data
            rating = int(form.rating.data)
            description = form.description.data
            notes = form.notes.data
            book = Book(title=title,
                author=author,
                genre=genre,
                rating=rating,
                cover=cover,
                bookpdf=pdf_book,
                description=description,
                notes=notes)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('create.html', form=form)
    elif not current_user.is_admin:
        return abort(404)

@app.route('/<int:book_id>/edit/', methods=('GET', 'POST'))
@login_required
def edit(book_id):
    if current_user.is_admin:
        book = Book.query.get_or_404(book_id)
        form = UpdateBook()
        if form.validate_on_submit():
            if form.cover.data:
                cover = save_picture(form.cover.data)
            else:
                cover = book.cover
            book.title = form.title.data
            book.author = form.author.data
            book.genre = form.genre.data
            book.rating = int(form.rating.data)
            book.description = form.description.data
            book.notes = form.notes.data
            try:
                db.session.commit()
                return redirect(url_for('index'))
            except IntegrityError:
                db.session.rollback()
                flash('Произошла ошибка: такая книга уже есть в базе', 'error')
                return render_template('edit.html', form=form)
      
            
        elif request.method == 'GET':
            form.title.data = book.title
            form.author.data = book.author
            form.genre.data = book.genre
            form.rating.data = book.rating
            form.cover.data = book.cover
            form.description.data = book.description
            form.notes.data = book.notes

        return render_template('edit.html', form=form)
    elif not current_user.is_admin:
        return abort(404)      

@app.post('/<int:book_id>/delete/')
@login_required
def delete(book_id):
    if current_user.is_admin:
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))
    elif not current_user.is_admin:
        return abort(404)   

@app.post('/<int:user_id>/delete/')
@login_required
def delete_user(user_id):
    if current_user.is_admin:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    elif not current_user.is_admin:
        return abort(404)


@app.route('/users/')
@login_required
def users():
    if current_user.is_admin:
        page = request.args.get('page', 1, type=int)
        users = User.query.filter().paginate(page=page, per_page=4)
        return render_template('users.html', users=users)
    elif not current_user.is_admin:
        return abort(404)


@app.route('/export/')
def data():
    #if current_user.is_admin:
    data = Book.query.all()

    return jsonify(data)
    #elif not current_user.is_admin:
        #return abort(404)  


@app.route('/read/')
@login_required
def read():
    return render_template('test.html')


@app.before_first_request
def create_tables():
    app.app_context().push()
    db.create_all()