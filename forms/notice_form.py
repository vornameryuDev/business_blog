from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class NoticeCreateForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('공지내용', validators=[DataRequired()])

class NoticeUpdateForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('공지내용', validators=[DataRequired()])