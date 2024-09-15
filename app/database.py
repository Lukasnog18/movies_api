from .schema import Movie, User

def create_mock_users():
    users = []

    users_data = [
        {
            'id': 1,
            'name': 'Lucas Nogueira',
            'phone': '8811111111',
            'email': 'email@mock.com',
        },
        {
            'id': 2,
            'name': 'Lucas Ferreira',
            'phone': '8822222222',
            'email': 'email@mock.com2',
        },
    ]

    for user_data in users_data:
        user = User(
            id=user_data['id'],
            name=user_data['name'],
            phone=user_data['phone'],
            email=user_data['email'],
        )
        users.append(user)

    return users



def create_mock_movies():
    movies = []
    
    movies_data = [
        {
            'id': 1,
            'title': 'The Godfather',
            'genre': ['Crime', 'Drama'],
            'year': '1972',
            'synopsis': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            'director': 'Francis Ford Coppola'
        },
        {
            'id': 2,
            'title': 'The Dark Knight',
            'genre': ['Action', 'Crime', 'Drama'],
            'year': '2008',
            'synopsis': 'When the menace known as the Joker emerges, he creates chaos in Gotham. Batman must accept one of the greatest psychological tests of his ability to fight injustice.',
            'director': 'Christopher Nolan'
        },
        {
            'id': 3,
            'title': 'Pulp Fiction',
            'genre': ['Crime', 'Drama'],
            'year': '1994',
            'synopsis': 'The lives of two mob hitmen, a boxer, a gangster, and his wife intertwine in a tale of violence and redemption.',
            'director': 'Quentin Tarantino'
        },
        {
            'id': 4,
            'title': 'Inception',
            'genre': ['Action', 'Adventure', 'Sci-Fi'],
            'year': '2010',
            'synopsis': 'A thief who steals corporate secrets through dream-sharing technology is given the task to plant an idea into the mind of a CEO.',
            'director': 'Christopher Nolan'
        },
        {
            'id': 5,
            'title': 'Fight Club',
            'genre': ['Drama'],
            'year': '1999',
            'synopsis': 'An insomniac office worker and a soap maker form an underground fight club that spirals out of control.',
            'director': 'David Fincher'
        },
        {
            'id': 6,
            'title': 'Forrest Gump',
            'genre': ['Drama', 'Romance'],
            'year': '1994',
            'synopsis': 'The story of Forrest Gump, a man with a low IQ, who witnesses and unwittingly influences several historical events in the 20th century.',
            'director': 'Robert Zemeckis'
        },
        {
            'id': 7,
            'title': 'The Matrix',
            'genre': ['Action', 'Sci-Fi'],
            'year': '1999',
            'synopsis': 'A hacker discovers the reality he lives in is a simulation, and joins a rebellion to overthrow the oppressive system.',
            'director': 'Lana Wachowski, Lilly Wachowski'
        },
        {
            'id': 8,
            'title': 'Interstellar',
            'genre': ['Adventure', 'Drama', 'Sci-Fi'],
            'year': '2014',
            'synopsis': 'A team of explorers travels through a wormhole in space in an attempt to ensure humanity\'s survival.',
            'director': 'Christopher Nolan'
        },
        {
            'id': 9,
            'title': 'Schindler\'s List',
            'genre': ['Biography', 'Drama', 'History'],
            'year': '1993',
            'synopsis': 'In German-occupied Poland during World War II, Oskar Schindler saves the lives of more than a thousand refugees.',
            'director': 'Steven Spielberg'
        },
        {
            'id': 10,
            'title': 'The Shawshank Redemption',
            'genre': ['Drama'],
            'year': '1994',
            'synopsis': 'Two imprisoned men form a deep friendship over several years, finding solace and redemption through acts of common decency.',
            'director': 'Frank Darabont'
        }
    ]
    
    for movie_data in movies_data:
        movie = Movie(
            id=movie_data['id'],
            title=movie_data['title'],
            genre=movie_data['genre'],
            year=movie_data['year'],
            synopsis=movie_data['synopsis'],
            director=movie_data['director']
        )
        movies.append(movie)

    return movies
