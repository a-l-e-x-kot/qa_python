import random
import pytest

from main import BooksCollector

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
        assert len(collector.get_books_genre()) == 2

        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_add_book_no_genre(self, collector):
        collector.add_new_book("teстирование dot COM")
        assert collector.books_genre["teстирование dot COM"] == ""


    def test_add_new_book_len_name_more_40(self, collector):
        collector.add_new_book('q' * 41)
        assert 'q' not in collector.books_genre


    def test_add_new_book_len_name_0(self, collector):
        collector.add_new_book('')
        assert '' not in collector.books_genre


    def test_set_book_genre_new_add_new_genre(self, collector):
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        assert collector.get_book_genre('Пикник на обочине') == 'Фантастика'


    def test_get_book_genre_get_genre(self, collector):
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        genre = collector.get_book_genre('Молчание ягнят')
        assert genre == 'Ужасы'

    def test_get_books_with_specific_genre_get_books_with_new_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert sorted(collector.get_books_with_specific_genre('Ужасы')) == sorted(
            ['Молчание ягнят', 'Гордость и предубеждение и зомби'])


    def test_get_books_genre_get_current_dictionaryv(self, collector):
        collector.add_new_book('teстирование dot COM')
        collector.add_new_book('Пикник на обочине')
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        result = collector.get_books_genre()
        books = {
            'teстирование dot COM': '',
            'Пикник на обочине': 'Фантастика',
            'Молчание ягнят': 'Ужасы'
        }
        assert books == result


    def test_get_books_for_children_not_age_limit(self, collector):
        collector.add_new_book('Голубой щенок')
        collector.set_book_genre('Голубой щенок', 'Мультфильмы')
        assert 'Голубой щенок' in collector.get_books_for_children()


    def test_get_books_for_children_with_age_limit(self, collector):
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        assert 'Молчание ягнят' not in collector.get_books_for_children()


    def test_add_book_in_favorites_add_favorites_book(self, collector):
        collector.add_new_book('Солёный пёс')
        collector.add_book_in_favorites('Солёный пёс')
        assert 'Солёный пёс' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_delete_favorites_book(self, collector):
        collector.add_new_book('Солёный пёс')
        collector.add_book_in_favorites('Солёный пёс')
        collector.delete_book_from_favorites('Солёный пёс')
        assert 'Солёный пёс' not in collector.favorites


    def test_get_list_of_favorites_books_list_books(self, collector):
        collector.add_new_book('Бегемот')
        collector.add_book_in_favorites('Бегемот')
        assert collector.get_list_of_favorites_books()
