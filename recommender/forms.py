from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    """
    Allows users to enter an COVID-19 article id
    """

    article_id = TextField(
        "Enter an article id, try with '00142f93c18b07350be89e96372d240372437ed9' ", validators=[DataRequired()]
    )
    submit = SubmitField("Find Related Articles")
