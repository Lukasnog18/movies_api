from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relacionamento com filmes alugados (tabela de associação)
    rentals = db.relationship('Rental', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    synopsis = db.Column(db.Text, nullable=True)
    director = db.Column(db.String(120), nullable=False)

    # Relacionamento com a tabela de associação de aluguel/avaliação
    rentals = db.relationship('Rental', backref='movie', lazy=True)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Tabela de Associação: Aluguel e Avaliação
class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    rental_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    rating = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Rental User: {self.user_id}, Movie: {self.movie_id}, Date: {self.rental_date}>'
