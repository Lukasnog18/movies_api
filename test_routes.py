import pytest
from flask_testing import TestCase
from app import create_app, db
from app.schema import Movie, User

class TestBase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

        user1 = User(id=1, name='Lucas Nogueira', phone='8811111111', email='email@mock.com')
        user2 = User(id=2, name='Lucas Ferreira', phone='8822222222', email='email@mock.com2')
        db.session.add(user1)
        db.session.add(user2)

        movie1 = Movie(id=1, title='The Godfather', genre='Crime, Drama', year='1972', synopsis='The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', director='Francis Ford Coppola')
        movie2 = Movie(id=2, title='The Dark Knight', genre='Action, Crime, Drama', year='2008', synopsis='When the menace known as the Joker emerges, he creates chaos in Gotham. Batman must accept one of the greatest psychological tests of his ability to fight injustice.', director='Christopher Nolan')
        db.session.add(movie1)
        db.session.add(movie2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestMovieAPI(TestBase):

    def test_get_movies(self):
        response = self.client.get('/movies/Action')
        self.assert200(response)
        self.assertIn('id', response.json[0])
        self.assertIn('title', response.json[0])
        self.assertIn('genre', response.json[0])

    def test_rent_movie(self):
        response = self.client.post('/rent/1/1')
        self.assert200(response)
        self.assertEqual(response.json['message'], 'Movie 1 rented successfully by user 1')

    def test_rent_movie_already_rented(self):
        self.client.post('/rent/1/1')
        response = self.client.post('/rent/1/1')
        self.assert400(response)
        self.assertEqual(response.json['error'], 'Movie already rented by this user')

    def test_rate_movie(self):
        self.client.post('/rent/1/1')
        response = self.client.post('/movies/1/rate', json={'user_id': 1, 'rating': 5})
        self.assert200(response)
        self.assertEqual(response.json['message'], 'Movie 1 rated 5 successfully by user 1')

    def test_get_user_rents(self):
        self.client.post('/rent/1/1')
        response = self.client.get('/user/1/rents')
        self.assert200(response)
        self.assertEqual(len(response.json), 1)
        self.assertIn('movie_id', response.json[0])
        self.assertIn('rental_date', response.json[0])

if __name__ == '__main__':
    pytest.main()
