import pytest
from src.item import Item


@pytest.fixture
def one_item():
    return Item('Toster', 10_000, 10)


def test_calculate_total_price(one_item):
    """
    Тест расчета общей стоимости товара
    """

    assert one_item.calculate_total_price() == 100_000


def test_apply_discount(one_item):
    """
    Тест применения скидки к товару
    """

    Item.pay_rate = 0.8
    one_item.apply_discount()
    assert one_item.price == 8000
