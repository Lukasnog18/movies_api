from flask import Blueprint, request, jsonify
from .schema import Rental
from .database import create_mock_movies, create_mock_users

bp = Blueprint('routes', __name__)

mock_users = create_mock_users()
mock_movies = create_mock_movies()
ALL_RENTS = []

# 1. Rota para listar filmes por gênero
@bp.route('/movies/<genre_name>', methods=['GET'])
def get_movies(genre_name):
    filtered_movies_by_genre = []
    for movie in mock_movies:
        movies_genres = [genre.upper() for genre in movie.genre]
        if genre_name.upper() in movies_genres:
            filtered_movies_by_genre.append(movie)

    return jsonify([movie.__dict__ for movie in filtered_movies_by_genre])

# 2. Rota para visualizar detalhes de um filme
@bp.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    movie = next((movie for movie in mock_movies if movie.id == movie_id), None)
    if movie:
        return jsonify(movie.__dict__)
    return jsonify({'error': 'Movie not found'}), 404

# 3. Rota para alugar um filme
@bp.route('/rent/<int:user_id>/<int:movie_id>', methods=['POST'])
def rent_movie(user_id, movie_id):
    # Checar se o filme já foi alugado
    if any(rent for rent in ALL_RENTS if rent.user_id == user_id and rent.movie_id == movie_id):
        return jsonify({'error': 'Movie already rented by this user'}), 400
    
    rent = Rental(
        user_id=user_id,
        movie_id=movie_id,
        rental_date='',
        rating=''
    )
    ALL_RENTS.append(rent)
    return jsonify([rent.__dict__ for rent in ALL_RENTS])

# 4. Rota para avaliar um filme alugado
@bp.route('/movies/<int:movie_id>/rate', methods=['POST'])
def rate_movie(movie_id):
    user_id = request.json.get('user_id')
    rating = request.json.get('rating')

    if not user_id or rating is None:
        return jsonify({'error': 'User ID and rating are required'}), 400

    # Verificar se o filme foi alugado por esse usuário
    rental = next((rent for rent in ALL_RENTS if rent.user_id == str(user_id) and rent.movie_id == str(movie_id)), None)
    if not rental:
        return jsonify({'error': 'This user has not rented this movie'}), 400

    # Adicionar a avaliação
    rental.rating = rating
    return jsonify({'message': f'Movie {movie_id} rated {rating} successfully'})

# 5. Rota para visualizar todos os filmes alugados por um usuário
@bp.route('/user/<user_id>/rents', methods=['GET'])
def get_user_rents(user_id):
    user = next((user for user in mock_users if user.id == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_rents = [rent for rent in ALL_RENTS if rent.user_id == user_id]
    rented_movies = [{
        'movie_id': rent.movie_id,
        'rating': rent.rating,
        'rental_date': rent.rental_date,
        'movie_details': next((movie.__dict__ for movie in mock_movies if movie.id == rent.movie_id), {})
    } for rent in user_rents]

    return jsonify(rented_movies)
