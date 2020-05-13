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
@login_required
def make_meal():
    form = MealsForm()
    if form.validate_on_submit():
        mealData = Meals(
            meal_name = form.meal_name.data,
            healthy = form.healthy.data,
            cook_length = form.cook_length.data,
            difficulty = form.difficulty.data,
            vegan = form.vegan.data,
            recipe = form.recipe.data
        )

        db.session.add(mealData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('make_meal.html', title='Create your own meal', form=form)