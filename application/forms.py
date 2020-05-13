from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MealsForm(FlaskForm):
    meal_name = StringField('Meal Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    healthy = StringField('How healthy is the meal?',
        validators = [
            DataRequired()
        ]
    )
    cook_length = StringField('Cooking time (mins)',
        validators = [
            DataRequired()
        ]
    )
    difficulty = StringField('Difficulty',
        validators = [
            DataRequired(),
            Length(min=2, max=15)
        ]
    )
    vegan = StringField('Suitable for vegans',
        validators = [
            DataRequired()
        ]
    )
    recipe = StringField('Recipe',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post!')