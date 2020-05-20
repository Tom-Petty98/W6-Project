from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class MealsForm(FlaskForm):
    meal_name = StringField('Meal Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    healthy = SelectField("How healthy is the meal?", [DataRequired()],
                        choices=[
                            (1, 'Very unhealthy'), 
                            (2, 'unhealthy'), 
                            (3, 'neutral'), 
                            (4, 'healthy'), 
                            (5, 'very healthy')]
    )
    cook_length = StringField('Cooking time (mins)',
        validators = [
            DataRequired()
        ]
    )
    difficulty = SelectField("Diffculty", [DataRequired()],
                        choices=["easy", "medium", "Hard"]
    )

    description = TextAreaField('Give a brief description of this meal',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    vegan = BooleanField('Suitable For Vegans')
    submit_meal = SubmitField('Post Meal!')



class IngredientsForm(FlaskForm):
    ingredient_name = StringField('Ingredient Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    shelf_life = SelectField("Shelf Life", [DataRequired()],
                        choices=["short", "medium", "long"]
    )

    vegan = BooleanField('Suitable For Vegans')
    submit_ingredient = SubmitField('Add ingredient!')
