from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Meals, Ingredients
from application.forms import MealsForm, IngredientsForm, AddIngredientsForm

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

    meal_form = MealsForm()
    if meal_form.validate_on_submit():
        mealData = Meals(
            meal_name = meal_form.meal_name.data,
            healthy = meal_form.healthy.data,
            cook_length = meal_form.cook_length.data,
            difficulty = meal_form.difficulty.data,
            vegan = meal_form.vegan.data,
            description = meal_form.description.data
        )

        db.session.add(mealData) 
        db.session.commit()

        return redirect(url_for('recipes'))

    #else:
       # print(form.errors)

    return render_template('make_meal.html', title='Create your own meal', meal_form=meal_form)


@app.route('/add_ingredients/<int:id>', methods=['GET', 'POST'])
def add_ingredients(id):
    # logic for getting the data for the meal selected

    meal = Meals.query.filter_by(id=id).first()

    add_ingredient_form = AddIngredientsForm()
    if add_ingredient_form.add_ingredient.data and add_ingredient_form.validate():
        ingredientData = Ingredients.query.filter_by(id = add_ingredient_form.ingredient.data).first()
        meal.ingredients.append(ingredientData)
        db.session.commit()
        return redirect(url_for('add_ingredients', id=id))

    ingredient_form = IngredientsForm()
    if ingredient_form.submit_ingredient.data and ingredient_form.validate():
        ingredientData = Ingredients(
            ingredient_name = ingredient_form.ingredient_name.data,
            shelf_life = ingredient_form.shelf_life.data,
            vegan = ingredient_form.vegan.data,
            )

        db.session.add(ingredientData) 
        meal.ingredients.append(ingredientData)  
        db.session.commit()
        return redirect(url_for('add_ingredients', id=id))

    return render_template('add_ingredients.html', title='Add Ingredients to your meal', ingredient_form=ingredient_form, add_ingredient_form=add_ingredient_form, meal=meal)


@app.route('/edit_meal/<int:id>', methods=['GET', 'POST'])
def edit_meal(id):

    meal = Meals.query.filter_by(id=id).first()

    meal_form = MealsForm()
    if meal_form.validate_on_submit():
        meal.meal_name = meal_form.meal_name.data
        meal.healthy = meal_form.healthy.data
        meal.cook_length = meal_form.cook_length.data
        meal.difficulty = meal_form.difficulty.data
        meal.vegan = meal_form.vegan.data
        meal.description = meal_form.description.data
        db.session.commit()
        return redirect(url_for('edit_meal', id=id))
    elif request.method == 'GET':
        meal_form.meal_name.data = meal.meal_name
        meal_form.healthy.data = meal.healthy
        meal_form.cook_length.data = meal.cook_length
        meal_form.difficulty.data = meal.difficulty
        meal_form.vegan.data = meal.vegan
        meal_form.description.data = meal.description

    return render_template('edit_meal.html', title='Edit meal', meal_form=meal_form, id=id)

@app.route('/delete_meal/<int:id>', methods=['GET', 'POST'])
def delete_meal(id):
    meal = Meals.query.filter_by(id=id).first()
    db.session.delete(meal)
    db.session.commit()
    return redirect(url_for('recipes'))

@app.route('/add_ingredients/delete_ingredient/<string:ids>', methods=['GET', 'POST'])
def delete_ingredient(ids):
    listIds = ids.split(',')
    ingredient = Ingredients.query.filter_by(id=int(listIds[1])).first()
    db.session.delete(ingredient)
    db.session.commit()
    return redirect(url_for('add_ingredients', id=int(listIds[0])))