from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'You Username'})
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 16)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')