from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
from application.models import Ingredients

class MealsForm(FlaskForm):
    meal_name = StringField('Meal Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    healthy = SelectField("How healthy is the meal?", [DataRequired()],
                        coerce=int,
                        choices=[
                            (1, 'Very Unhealthy'), 
                            (2, 'Unhealthy'), 
                            (3, 'Neutral'), 
                            (4, 'Healthy'), 
                            (5, 'Very Healthy')]
    )
    cook_length = StringField('Cooking time (mins)',
        validators = [
            DataRequired()
        ]
    )
    difficulty = SelectField("Diffculty", [DataRequired()],
                        choices=[("easy", "easy"), ("medium", "medium"), ("hard", "hard")]
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
                        choices=[("short", "short"), ("medium", "medium"), ("long", "long")]
    )

    vegan = BooleanField('Suitable For Vegans')
    submit_ingredient = SubmitField('Add ingredient!')

class AddIngredientsForm(FlaskForm):
    ingredient = SelectField('Add some Ingredients',
                                   coerce=int,
                                   choices=[(i.id, i.ingredient_name) for i in Ingredients.query.all()]
    )
    add_ingredient = SubmitField('Add ingredient!')