import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_two_book_with_genre(collector):
    collector.add_new_book('Мир')
    collector.add_new_book('Сияние')
    collector.set_book_genre('Мир', 'Фантастика')
    collector.set_book_genre('Сияние', 'Ужасы')
    return collector


@pytest.fixture
def book_in_favorites(collector):
    collector.add_new_book('Хрустальный горизонт')
    collector.add_book_in_favorites('Хрустальный горизонт')
    return collector
