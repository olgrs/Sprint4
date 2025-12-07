import pytest
from test_data import BOOKS_FANTASTIC_AND_SCARY


class TestBooksCollector:
    @pytest.mark.parametrize('title', [
        'А',
        'Преступление и наказание',
        'A' * 40
        ])
    def test_add_new_book_valid_title(self, collector, title):
        collector.add_new_book(title)
        assert len(collector.books_genre) == 1

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_not_add_same_book(self, collector):
        collector.add_new_book('Хрустальный горизонт')
        collector.add_new_book('Хрустальный горизонт')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('title', ['', 'A' * 41])
    def test_add_new_book_not_valid_title_length(self, collector, title):
        collector.add_new_book(title)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_set_valid_genre(self, collector):
        collector.add_new_book('Мир')
        collector.set_book_genre('Мир', 'Фантастика')
        assert collector.books_genre['Мир'] == 'Фантастика'

    def test_set_book_genre_not_set_unknown_genre(self, collector):
        collector.add_new_book('Мир')
        collector.set_book_genre('Мир', 'Романтика')
        assert collector.books_genre['Мир'] == ''

    def test_set_book_genre_not_set_unknown_book(self, collector):
        collector.set_book_genre('Лишняя книга', 'Ужасы')
        assert 'Ужасы' not in collector.books_genre

    def test_get_book_genre_valid_book_and_genre(self, collector):
        collector.add_new_book('Мир')
        collector.set_book_genre('Мир', 'Фантастика')
        result = collector.get_book_genre('Мир')
        assert result == 'Фантастика'

    def test_get_book_genre_unknown_book(self, collector):
        result = collector.get_book_genre('Лишняя книга')
        assert result is None

    def test_get_books_with_specific_genre_list(
            self,
            collector,
            add_two_books_fantastic_and_scary
            ):
        expected = [
            title
            for title, genre in BOOKS_FANTASTIC_AND_SCARY.items()
            if genre == 'Фантастика'
        ]
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == expected

    def test_get_books_genre_full_dict(
            self,
            collector,
            add_two_books_fantastic_and_scary
            ):
        assert collector.get_books_genre() == BOOKS_FANTASTIC_AND_SCARY

    def test_get_books_for_children_filter_genre_age(
            self,
            collector,
            add_two_books_fantastic_and_scary
            ):
        expected = [
            title
            for title, genre in BOOKS_FANTASTIC_AND_SCARY.items()
            if genre not in collector.genre_age_rating
        ]
        result = collector.get_books_for_children()
        assert result == expected

    def test_add_book_in_favorites_add_book(
            self,
            collector,
            book_in_favorites
            ):
        assert collector.favorites == ['Хрустальный горизонт']

    def test_add_book_in_favorites_not_add_same_book(
            self,
            collector,
            book_in_favorites
            ):
        collector.add_book_in_favorites('Хрустальный горизонт')
        assert collector.favorites == ['Хрустальный горизонт']

    def test_delete_book_from_favorites_one_book_deleted(
            self,
            collector,
            book_in_favorites
            ):
        collector.delete_book_from_favorites('Хрустальный горизонт')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_return_list(
            self,
            collector,
            book_in_favorites
            ):
        assert collector.get_list_of_favorites_books() == [
            'Хрустальный горизонт'
            ]
