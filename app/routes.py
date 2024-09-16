from flask import Blueprint, request, jsonify
from .schema import User, Movie, rental_table
from app import db
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/movies/<genre_name>', methods=['GET'])
def get_movies(genre_name):
    genre_name = genre_name.lower()
    movies = Movie.query.all()
    
    filtered_movies_by_genre = []
    for movie in movies:
        movie_genres = [genre.strip().lower() for genre in movie.genre.split(',')]
        if genre_name in movie_genres:
            filtered_movies_by_genre.append(movie)

    return jsonify([{
        'id': movie.id,
        'title': movie.title,
        'genre': movie.genre,
        'year': movie.year,
        'synopsis': movie.synopsis,
        'director': movie.director
    } for movie in filtered_movies_by_genre])

@bp.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        return jsonify({
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'year': movie.year,
            'synopsis': movie.synopsis,
            'director': movie.director
        })
    return jsonify({'error': 'Movie not found'}), 404

@bp.route('/rent/<int:user_id>/<int:movie_id>', methods=['POST'])
def rent_movie(user_id, movie_id):
    existing_rent = db.session.query(rental_table).filter_by(user_id=user_id, movie_id=movie_id).first()
    if existing_rent:
        return jsonify({'error': 'Movie already rented by this user'}), 400

    rental_date = datetime.now().strftime('%d/%m/%Y')
    rent = {
        'user_id': user_id,
        'movie_id': movie_id,
        'rental_date': rental_date,
        'rating': ''
    }

    db.session.execute(rental_table.insert().values(rent))
    db.session.commit()

    return jsonify({'message': f'Movie {movie_id} rented successfully by user {user_id}'}), 200

@bp.route('/movies/<int:movie_id>/rate', methods=['POST'])
def rate_movie(movie_id):
    user_id = request.json.get('user_id')
    rating = request.json.get('rating')

    if not user_id or rating is None:
        return jsonify({'error': 'User ID and rating are required'}), 400

    rental = db.session.query(rental_table).filter_by(user_id=user_id, movie_id=movie_id).first()
    if not rental:
        return jsonify({'error': 'This user has not rented this movie'}), 400

    db.session.execute(rental_table.update().where(rental_table.c.user_id == user_id).where(rental_table.c.movie_id == movie_id).values(rating=rating))
    db.session.commit()

    return jsonify({'message': f'Movie {movie_id} rated {rating} successfully by user {user_id}'}), 200

@bp.route('/user/<int:user_id>/rents', methods=['GET'])
def get_user_rents(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    rents = db.session.query(rental_table).filter_by(user_id=user_id).all()
    rented_movies = [{
        'movie_id': rent.movie_id,
        'rating': rent.rating,
        'rental_date': rent.rental_date,
        'movie_details': {
            'title': Movie.query.get(rent.movie_id).title,
            'genre': Movie.query.get(rent.movie_id).genre,
            'year': Movie.query.get(rent.movie_id).year,
            'synopsis': Movie.query.get(rent.movie_id).synopsis,
            'director': Movie.query.get(rent.movie_id).director
        }
    } for rent in rents]

    return jsonify(rented_movies)

def init_app(app):
    app.register_blueprint(bp)
