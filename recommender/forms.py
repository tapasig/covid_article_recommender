from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    """
    Allows users to enter an COVID-19 article id
    """
    article_id = StringField(
        "Enter an article id ", validators=[DataRequired()]
    )
    submit = SubmitField("Find related articles")
