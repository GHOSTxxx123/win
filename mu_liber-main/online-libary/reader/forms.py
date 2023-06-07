from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, BooleanField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Email
from reader.models import Book, User

class BookForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Автор', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Жанр', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Обложка книги', validators=[FileAllowed(['jpg', 'png'])])
    bookpdf = FileField('Файл книги (pdf)', validators=[DataRequired(),
                                                            FileAllowed(['pdf'])])
    rating = IntegerField('Моя оценка', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Сюжет',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Заметки',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Добавить')

    def validate_title(self, title):
        title = Book.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('Такая книга уже есть в списке прочитанных.')


class UpdateBook(FlaskForm):
    title = StringField('Название', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Автор', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Жанр', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Обложка книги', validators=[FileAllowed(['jpg', 'png'])])
    rating = IntegerField('Моя оценка', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Сюжет',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Заметки',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Обновить')



class Sign_in(FlaskForm):
    name = StringField('Номер читательского билета', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    remember = BooleanField("Запомнить меня")                                        
    submit = SubmitField('Вход')         


class Sign_up(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),
                                             Length(min=2, max=100)])
    firstname = StringField('Фамилия', validators=[DataRequired(),
                                             Length(min=2, max=100)])                                        
    gmail = StringField('Ведите Gmail',validators = [Email()])
    readbilet = StringField('Ведите номер читательского билета ', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                             Length(min=8, max=100)])                                                                                
    kyrs = IntegerField('Ведите курс', validators=[DataRequired(), NumberRange(min=1, max=4)])

    submit = SubmitField('Авторизация')                                             
    
    def validate_readbilet(self, readbilet):
        readbilet = User.query.filter_by(readbilet=readbilet.data).first()
        if readbilet:
            raise ValidationError('Номер читательского билета уже используется')











