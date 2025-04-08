"""
Протестируйте классы из модуля homework/models.py
"""

import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    @pytest.mark.parametrize("test", [1000, 500, 1])
    def test_product_check_quantity(self, product, test):
        assert product.check_quantity(test)

    @pytest.mark.parametrize("test", [999, 500, 1])
    def test_product_buy(self, product,test):
        result_q = product.buy(test)
        assert product.quantity == result_q

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:

    def test_cart_add_product(self, cart, product):
        # Добавление товара в корзину
        cart.add_product(product)
        # Счетчик увеличился на 1
        assert cart.products[product] == 1

        cart.add_product(product, 3)
        # Счётчик увеличился на 3
        assert cart.products[product] == 4

    def test_cart_remove_product(self, cart, product):
        # Удаляем 1 продукт
        cart.add_product(product,4)
        assert cart.products[product] == 4
        cart.remove_product(product, 1)
        assert cart.products[product] == 3
        # Удаляем все
        cart.remove_product(product)

    def test_cart_clear(self,cart, product):
        cart.add_product(product, 8)
        cart.clear()
        assert cart.products == {}

    def test_cart_get_total_price(self,cart, product):
        cart.add_product(product, 100)
        price = cart.get_total_price()
        assert price == 10000

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 100)
        cart.buy(100)
        assert cart.products == {}
        assert product.quantity == 900

    def test_cart_buy_more_than_availeble(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy(1001)