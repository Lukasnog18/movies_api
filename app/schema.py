from app import db

# Tabela intermediária para o relacionamento muitos-para-muitos
rental_table = db.Table('rentals',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('rental_date', db.String(50), nullable=False),
    db.Column('rating', db.String(5), nullable=True)
)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relacionamento com filmes através da tabela intermediária
    rented_movies = db.relationship('Movie', secondary=rental_table, lazy='subquery',
                                    backref=db.backref('rented_by', lazy=True))

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(250), nullable=False)  # Armazenado como string delimitada
    year = db.Column(db.String(4), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    director = db.Column(db.String(120), nullable=False)

    # Filmes alugados serão acessados por meio do relacionamento
