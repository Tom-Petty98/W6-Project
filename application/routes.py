from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Meals
from application.forms import MealsForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/recipes')
def recipes():
    mealData = Meals.query.all()
    return render_template('recipes.html', title="Recipes", meals=mealData)


@app.route('/make_meal', methods=['GET', 'POST'])
def make_meal():
    meal_form = MealsForm()
    if form.validate_on_submit() and meal_form.submit_meal.data:
        mealData = Meals(
            meal_name = meal_form.meal_name.data,
            healthy = meal_form.healthy.data,
            cook_length = meal_form.cook_length.data,
            difficulty = meal_form.difficulty.data,
            vegan = meal_form.vegan.data,
            recipe = meal_form.recipe.data
        )

        db.session.add(mealData)
        # mealData.ingredients.append(...)  not sure how im going to capture ingredients yet but could be outputted with a for loop.
        db.session.commit()

        return redirect(url_for('recipes'))

    else:
        print(form.errors)

    return render_template('make_meal.html', title='Create your own meal', meal_form, ingredient_form)
