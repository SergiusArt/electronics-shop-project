import pytest
from src.keyboard import Keyboard


@pytest.fixture
def my_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(my_keyboard):
    """
    Магический метод str должен возвращать имя клавиатуры
    """

    assert str(my_keyboard) == "Dark Project KD87A"


def test_language(my_keyboard):
    """
    Возвращает текущий язык раскладки клавиатуры
    """

    assert str(my_keyboard.language) == "EN"

    my_keyboard.change_lang()
    assert str(my_keyboard.language) == "RU"

    # Сделали RU -> EN -> RU
    my_keyboard.change_lang().change_lang()
    assert str(my_keyboard.language) == "RU"
