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


def test_name(one_item):
    """
    Проверяем, как работает вызов метода-атрибута имени и как длина имени обрезается на 10 символах
    """

    assert one_item.name == 'Toster'

    one_item.name = 'СуперСмартфон'
    assert one_item.name == 'СуперСмарт'


def test_instantiate_from_csv(one_item):
    """
    Проверяем создание объектов из данных файлов формата csv
    """

    one_item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(one_item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = one_item.all[0]
    assert item1.name == 'Смартфон'

    assert one_item.string_to_number('5') == 5
    assert one_item.string_to_number('5.0') == 5
    assert one_item.string_to_number('5.5') == 5


def test_repr(one_item):
    """
    Магический метод repr должен возвращать название класса и его атрибуты инициализации
    """
    assert repr(one_item) == "Item('Toster', 10000, 10)"


def test_str(one_item):
    """
    Магический метод str должен возвращать имя экземпляра
    """

    assert str(one_item) == 'Toster'
