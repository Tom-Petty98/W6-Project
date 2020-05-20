from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Meals
from application.forms import MealsForm, IngredientsForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/recipes')
def recipes():
    mealData = Meals.query.all()
    return render_template('recipes.html', title="Meals", meals=mealData)


@app.route('/make_meal', methods=['GET', 'POST'])
def make_meal():
    form = MealsForm()
    if form.validate_on_submit():
        mealData = Meals(
            meal_name = form.meal_name.data,
            healthy = form.healthy.data,
            cook_length = form.cook_length.data,
            difficulty = form.difficulty.data,
            vegan = form.vegan.data,
            description = form.description.data
        )

        db.session.add(mealData) 
        db.session.commit()

        return redirect(url_for('recipes'))

    else:
        print(form.errors)

    return render_template('make_meal.html', title='Create your own meal', form=form)

@app.route('/add_ingredients', methods=['GET', 'POST'])
def add_ingredients():
    # logic for getting the data for the meal selected

    ingredient_form = IngredientsForm()
    if form.validate_on_submit():
        ingredientData = Ingredients(
            ingredient_name = ingredient_form.ingredient_name.data,
            shelf_life = ingredient_form.shelf_life.data,
            vegan = ingredient_form.vegan.data,
            )

            # need to add logic for selecting what meal to append to
        db.session.add(ingredientData) 
        mealData.ingredients.append(ingredientData)  

    return render_template('add_ingredients.html', title='Add Ingredients to your meal', form=ingredient_form)