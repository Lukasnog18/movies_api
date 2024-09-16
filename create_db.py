from app import create_app
from app.database import create_mock_users, create_mock_movies

app = create_app()

with app.app_context():
    create_mock_users()
    create_mock_movies()
