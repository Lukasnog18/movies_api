import os

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'movies_db')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'db')  # This is the service name defined in docker-compose.yaml
POSTGRES_PORT = 5432

SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False