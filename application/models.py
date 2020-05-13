from application import db

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(30), nullable=False, unique=True)
    healthy = db.Column(db.Float, nullable=False)
    difficulty = db.Column(db.String(15), nullable=False)
    cook_length = db.Column(db.Integer, nullable=False)
    recipe = db.Column(db.String(500), nullable=False, unique=True)
#   meal_image = db.Column(db.String(100, nullable=True, unique=True))
    vegan = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return ''.join([
            'Meal: ', self.meal_name, ' ', self.id,
            ])