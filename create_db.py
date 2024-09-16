from app import create_app
from app.database import create_mock_users, create_mock_movies, db

app = create_app()

with app.app_context():
    db.create_all()
    create_mock_users()
    create_mock_movies()
