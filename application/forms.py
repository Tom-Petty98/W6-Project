from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
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
    recipe = StringField('Recipe',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )

    vegan = BooleanField('Suitable For Vegans')
    submit = SubmitField('Post Meal!')
