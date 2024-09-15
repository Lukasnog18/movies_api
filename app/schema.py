from dataclasses import dataclass
from typing import List

@dataclass
class User:
    id: int
    name: str
    phone: str
    email: str

@dataclass
class Movie:
    id: int
    title: str
    genre: List[str]
    year: str
    synopsis: str
    director: str

@dataclass
class Rental:
    user_id: int
    movie_id: int
    rental_date: str
    rating: str
