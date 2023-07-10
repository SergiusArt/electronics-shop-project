import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def my_phone():
    return Phone('IPhone_14', 100000, 500, 2)


def test_repr(my_phone):
    """
    Магический метод repr должен возвращать название класса и его атрибуты инициализации
    """

    assert repr(my_phone) == "Phone('IPhone_14', 100000, 500, 2)"


def test_str(my_phone):
    """
    Магический метод str должен возвращать имя экземпляра
    """

    assert str(my_phone) == 'IPhone_14'


def test_sim(my_phone):
    assert my_phone.number_of_sim == 2
    my_phone.number_of_sim = 1
    assert my_phone.number_of_sim == 1
    my_phone.number_of_sim = 0
    assert my_phone.number_of_sim == 1
