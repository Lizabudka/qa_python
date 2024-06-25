from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre.keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем в __init__ список жанров
    def test_genre_of_books_true(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # проверяем в __init__ рейтинг
    def test_genre_age_rating_true(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # проверяем, проставляется ли жанр для книги
    def test_set_book_genre_set_one_genre(self, collector, murder_in_the_orient_express):
        assert collector.get_book_genre(murder_in_the_orient_express) == 'Детективы'

    # проверяем жанр, не указанный в классе
    def test_set_book_genre_set_non_existed_genre_none(self, collector):
        collector.add_new_book('Маша и медведь')
        assert collector.set_book_genre('Маша и медведь', 'Сказка') is None

    # проверяем вывод книг по жанру
    def test_get_books_with_specific_genre_get_two_detectives(self, collector,
                                                              murder_in_the_orient_express,
                                                              sherlock_holmes,
                                                              steven_king_it):
        # добавила книгу ужасы, чтобы проверить, что метод не выводит все подряд
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    # проверяем вывод книг по жанру, если таких книг нет
    def test_get_books_with_specific_genre_zero_books_for_genre(self, collector):
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    # проверяем список добавленных книг
    def test_get_books_genre_get_two_books(self, collector, murder_in_the_orient_express, steven_king_it):
        steven_king_it = steven_king_it
        assert murder_in_the_orient_express in collector.get_books_genre() and steven_king_it in collector.get_books_genre()

    # проверяем вывод книг для детей
    @pytest.mark.parametrize('book_name, book_genre',
                             [['Винни Пух', 'Мультфильмы'],
                              ['Хоббит', 'Фантастика'],
                              ['Двенадцать стульев', 'Комедии']])
    def test_get_books_for_children_get_one_book(self, book_name, book_genre, collector, steven_king_it):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        # добавила книгу ужасы, чтобы проверить, что метод не выводит все подряд
        assert collector.get_books_for_children()[0] == book_name and len(collector.get_books_for_children()) == 1

    # проверяем добавление книг в избранные
    def test_add_book_in_favorites_add_two_books(self, collector, steven_king_it,
                                                 murder_in_the_orient_express, sherlock_holmes):
        # добавлена "лишняя" контрольная книга, которая не будет добавлена в любимые

        collector.add_book_in_favorites(murder_in_the_orient_express)
        collector.add_book_in_favorites(steven_king_it)

        fav_books = collector.get_list_of_favorites_books()

        assert (len(fav_books) == 2) and (murder_in_the_orient_express in fav_books) and (steven_king_it in fav_books)

    # проверяем удаление книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self, collector,
                                                        steven_king_it, murder_in_the_orient_express):
        collector.add_book_in_favorites(murder_in_the_orient_express)
        collector.add_book_in_favorites(steven_king_it)

        collector.delete_book_from_favorites(murder_in_the_orient_express)

        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books()[0] == steven_king_it
