from application import db

#child table
meal_ingredients = db.Table('meal_ingredients',
    db.Column('meal_id', db.Integer, db.ForeignKey('meals.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'))
)

class Meals(db.Model):         
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(30), nullable=False, unique=True)
    healthy = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(15), nullable=False)
    cook_length = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False, unique=True)
#   meal_image = db.Column(db.String(100, nullable=True, unique=True))
    vegan = db.Column(db.Boolean, nullable=False)
    ingredients = db.relationship('Ingredients', secondary=meal_ingredients, backref="meals", lazy = True)

    def __repr__(self):
        return ''.join([
            'Meal: ', self.meal_name, ' ', self.id,
            ])


class Ingredients(db.Model):        
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(30), nullable=False, unique=True)
    shelf_life = db.Column(db.String(15), nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return ''.join([
            'Ingredient: ', self.ingredient_name, ' ', self.id,
            ])

