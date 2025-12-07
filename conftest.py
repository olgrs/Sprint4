import pytest
from main import BooksCollector
from test_data import FAVORITE_BOOK, BOOKS_FANTASTIC_AND_SCARY


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_two_books_fantastic_and_scary(collector):
    for title, genre in BOOKS_FANTASTIC_AND_SCARY.items():
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
    return collector


@pytest.fixture
def add_favorite_book(collector):
    collector.add_new_book(FAVORITE_BOOK)
    return collector
