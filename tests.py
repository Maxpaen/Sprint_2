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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_has_raiting_1(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавленная книга имеет рейтинг 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    @pytest.mark.parametrize('rating', [1,2,3,4,5,6,7,8,9,10])
    def test_set_book_rating_accepts_range_from_1_to_10(self, rating):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', rating)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == rating

    @pytest.mark.parametrize('rating', [0,11])
    def test_set_book_rating_doest_accept_value_0_and_11(self, rating):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', rating)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating_shows_books_with_rating_9(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        assert collector.get_books_with_specific_rating(9)[0] == 'Что делать, если ваш кот хочет вас убить' and len(collector.get_books_with_specific_rating(9)) == 1

    def test_get_books_rating_return_dict(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Армагеддон')
        # assert collector.get_books_rating()['Гордость и предубеждение и зомби'] == 1 and collector.get_books_rating()['Армагеддон'] == 1
        assert list(collector.get_books_rating().keys())[0] == 'Гордость и предубеждение и зомби' and list(collector.get_books_rating().keys())[2] == 'Армагеддон' and len(collector.get_books_rating().keys()) == 3

    def test_add_book_in_favorites_book_added_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books()[0] == 'Гордость и предубеждение и зомби'

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_return_array(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1
