from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Username', validators=[Required()])
    room = StringField('Room-ID', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
