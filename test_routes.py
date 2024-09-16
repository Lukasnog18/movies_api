import pytest
from flask_testing import TestCase
from app import create_app, db

class TestBase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        """Configura o ambiente de teste antes de cada teste"""
        db.create_all()
        # Adicione dados iniciais de teste aqui, se necessário

    def tearDown(self):
        """Limpa o ambiente de teste após cada teste"""
        db.session.remove()
        db.drop_all()

class TestMovieAPI(TestBase):

    def test_get_movies(self):
        """Testa a rota para obter filmes por gênero"""
        response = self.client.get('/movies/Action')
        self.assert200(response)
        self.assertIn('id', response.json[0])
        self.assertIn('title', response.json[0])
        self.assertIn('genre', response.json[0])

    def test_rent_movie(self):
        """Testa a rota para alugar um filme"""
        response = self.client.post('/rent/1/1')
        self.assert200(response)
        self.assertEqual(len(response.json), 1)
        self.assertIn('rental_date', response.json[0])
        self.assertIn('rating', response.json[0])

    def test_rent_movie_already_rented(self):
        """Testa a tentativa de alugar um filme já alugado"""
        self.client.post('/rent/1/1')
        response = self.client.post('/rent/1/1')
        self.assert400(response)
        self.assertEqual(response.json['error'], 'Movie already rented by this user')

    def test_rate_movie(self):
        """Testa a rota para avaliar um filme"""
        self.client.post('/rent/1/1')
        response = self.client.post('/movies/1/rate', json={'user_id': 1, 'rating': 5})
        self.assert200(response)
        self.assertEqual(response.json['message'], 'Movie 1 rated 5 successfully')

    def test_get_user_rents(self):
        """Testa a rota para obter os aluguéis de um usuário"""
        self.client.post('/rent/1/1')
        response = self.client.get('/user/1/rents')
        self.assert200(response)
        self.assertEqual(len(response.json), 1)
        self.assertIn('movie_id', response.json[0])
        self.assertIn('rental_date', response.json[0])

if __name__ == '__main__':
    pytest.main()
