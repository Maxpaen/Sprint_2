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
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, "Default rating for just added book not 1"

    @pytest.mark.parametrize('rating', [1,5,10])
    def test_set_book_rating_accepts_value_1_5_10(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', rating)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == rating, "set_book_rating method does not accept value 1, 5 or 10"

    @pytest.mark.parametrize('rating', [0,11])
    def test_set_book_rating_doest_accept_value_0_and_11(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', rating)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, "set_book_rating method accept value 0 or 11"

    def test_get_books_with_specific_rating_return_books_with_rating_9(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_rating(9), "Book with rating 9 is not in list"

    def test_get_books_rating_return_dict_with_correct_amount(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Армагеддон')
        assert len(collector.get_books_rating()) == 3, "books_rating_return method return dictionary with not 3 elements"

    def test_add_book_in_favorites_book_added_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books()[0] == 'Гордость и предубеждение и зомби', "Book was not added in favorites"

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0, "Book was not deleted from favorites"
