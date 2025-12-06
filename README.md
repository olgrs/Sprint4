# Sprint_4

## Реализованные тесты для BooksCollector


- `test_add_new_book_valid_title` — проверка добавления книги с корректным названием (короткое и длинное ≤ 40 символов)  
- `test_add_new_book_add_two_books` — добавление двух разных книг  
- `test_add_new_book_not_add_same_book` — проверка, что одну и ту же книгу нельзя добавить дважды  
- `test_add_new_book_not_valid_title_length` — проверка, что книга с пустым или слишком длинным названием (>40) не добавляется  


- `test_set_book_genre_set_valid_genre` — установка корректного жанра для существующей книги  
- `test_set_book_genre_not_set_unknown_genre` — попытка установки неизвестного жанра (не меняет жанр)  
- `test_set_book_genre_not_set_unknown_book` — попытка установки жанра для неизвестной книги  


- `test_get_book_genre_valid_book_and_genre` — получение жанра существующей книги  
- `test_get_book_genre_unknown_book` — получение жанра несуществующей книги (возвращает `None`)  


- `test_get_books_with_specific_genre_list` — получение списка книг с заданным жанром  
- `test_get_books_genre_full_dict` — получение полного словаря книг и их жанров  
- `test_get_books_for_children_filter_genre_age` — фильтрация книг с учётом возрастного ограничения  


- `test_add_book_in_favorites_add_book` — добавление книги в избранное  
- `test_add_book_in_favorites_not_add_same_book` — попытка повторного добавления книги в избранное (не дублируется)  
- `test_delete_book_from_favorites_one_book_deleted` — удаление книги из избранного  
- `test_get_list_of_favorites_books_return_list` — получение списка избранных книг
