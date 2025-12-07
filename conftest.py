import pytest
from main import BooksCollector
from test_data import BOOKS_FANTASTIC_AND_SCARY


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
def book_in_favorites(collector):
    collector.add_new_book('Хрустальный горизонт')
    collector.add_book_in_favorites('Хрустальный горизонт')
    return collector
