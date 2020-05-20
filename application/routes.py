from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Meals, Ingredients
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

    ingredient_form = IngredientsForm()
    if ingredient_form.submit_ingredient.data and ingredient_form.validate():
        ingredientData = Ingredients(
            ingredient_name = ingredient_form.ingredient_name.data,
            shelf_life = ingredient_form.shelf_life.data,
            vegan = ingredient_form.vegan.data,
            )
        db.session.add(ingredientData)
        db.session.commit()

    meal_form = MealsForm()
    if meal_form.submit_meal.data and meal_form.validate():
        mealData = Meals(
            meal_name = meal_form.meal_name.data,
            healthy = meal_form.healthy.data,
            cook_length = meal_form.cook_length.data,
            difficulty = meal_form.difficulty.data,
            vegan = meal_form.vegan.data,
            description = meal_form.description.data
        )

        db.session.add(mealData) 

        for i in request.form.getlist('ingredients'):
            mealData.ingredients.append(Ingredients.query.filter_by(id=i).first())

        db.session.commit()

        return redirect(url_for('recipes'))

    #else:
       # print(form.errors)

    return render_template('make_meal.html', title='Create your own meal', meal_form=meal_form, ingredient_form=ingredient_form)

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