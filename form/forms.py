from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, FileField, FileRequired, \
    FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'You Username'})
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 16)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()

    def validate_answer(form, field):
        if field.data != 42:
            raise ValidationError('Must be 42.')
    
class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif'])])
    submit = SubmitField()

