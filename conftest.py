import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope='function')
def murder_in_the_orient_express(collector):
    murder_in_the_orient_express = 'Убийство в восточном экспрессе'

    collector.add_new_book(murder_in_the_orient_express)
    collector.set_book_genre(murder_in_the_orient_express, 'Детективы')

    return murder_in_the_orient_express


@pytest.fixture(scope='function')
def sherlock_holmes(collector):
    sherlock_holmes = 'Рассказы о Шерлоке Холмсе'

    collector.add_new_book(sherlock_holmes)
    collector.set_book_genre(sherlock_holmes, 'Детективы')

    return sherlock_holmes


@pytest.fixture(scope='function')
def steven_king_it(collector):
    steven_king_it = 'Оно'

    collector.add_new_book(steven_king_it)
    collector.set_book_genre(steven_king_it, 'Ужасы')

    return steven_king_it
