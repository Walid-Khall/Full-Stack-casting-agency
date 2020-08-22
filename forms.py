from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SelectField,
                     SelectMultipleField,
                     DateTimeField,
                     BooleanField
                     )
from wtforms.validators import DataRequired, AnyOf, URL, Regexp


class MovieForm(FlaskForm):
    title = StringField(
        'title', validators=[DataRequired()]
    )
    release = StringField(
        'release', validators=[DataRequired()]
    )


class ActorForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    gender = StringField(
        'gender', validators=[DataRequired()]
    )
    age = StringField(
        'age', validators=[DataRequired()]
    )
