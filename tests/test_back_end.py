import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Meals, Ingredients
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('PROJECT_TESTING_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

    def premade_meal(self):
        return self.client.post(
            '/make_meal',
            data=dict(
                meal_name = 'Test meal',
                healthy = 3,
                cook_length = 50,
                difficulty = 'Easy',
                vegan = True,
                description = 'Meal description'
                ),
            follow_redirects=True
        )

    def make_meal(self, meal_name, healthy, cook_length, difficulty, vegan, description):
        return self.client.post(
        '/make_meal',
        data=dict(
            meal_name=meal_name, healthy=healthy, cook_length=cook_length, 
            difficulty=difficulty, vegan=vegan, description=description
            ),
        follow_redirects=True
        )

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('recipes'))
        self.assertEqual(response.status_code, 200)


class TestPosts(TestBase):

    def test_add_new_meal(self):
        """
        Test that when I add a new meal, I am redirected to the recipes page with the new recipe visible
        """
        with self.client:
            response = self.premade_meal()
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test meal', response.data)

    def test_edit_meal(self):
        self.premade_meal()
        response = self.client.post(
            '/edit_meal/1',
            data=dict(
                description='Edited meal',                 # editing multiple aspects doesn't change covarge 
            ),
            follow_redirects=True
        )
        self.assertIn(b'Edited meal', response.data)

    def test_add_ingredients(self):
        self.premade_meal()
        response = self.client.post(
            'add_ingredients/1',
            data=dict(
                ingredient_name='Pasta',
                shelf_life='long',
                vegan=True
            ),
            follow_redirects=True
        )
        self.assertIn(b'Pasta', response.data)

    def test_delete_meal(self):
        self.premade_meal()
        original = Meals.query.count()
        self.client.post(
            '/delete_meal/1',
            follow_redirects=True
        )
        assert original != Meal.query.count()
           # self.assertEqual(response.status_code, 200)
        


    def test_delete_ingredients(self):
        self.premade_meal()
        self.client.post(
            'add_ingredients/1',
            data=dict(
                ingredient_name='Pasta',
                shelf_life='long',
                vegan=True
            ),
            follow_redirects=True
        )
        with self.client:
            response =self.client.post(
                '/add_ingredients/delete_ingredient/1,1',
                follow_redirects=True 
            )
            self.assertEqual(response.status_code, 200)


# duplicate meal name
# duplicate ingredient name   currently should be a 500 error response
# add ingredient
# post requests are 302        get 200


class TestModels(TestBase):

    def test_meal_repr_model(self):
        meal = Meals(meal_name='Test meal', healthy=3, cook_length=50, difficulty='Easy', description='Meal description')
        assert repr(meal) == 'Meal: Test meal 1'