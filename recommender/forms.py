from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    """
    Allows users to enter an COVID-19 article id
    """

    article_id = TextField(
        "Enter an article id, try with '000b7d1517ceebb34e1e3e817695b6de03e2fa78' ", validators=[DataRequired()]
    )
    submit = SubmitField("Find Related Articles")
