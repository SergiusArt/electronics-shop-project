from src.item import Item


class Mixin_change_lang:
    """
    Функционал, который хранит и изменяет раскладку клавиатуры
    """

    def __init__(self):
        """
        Инициализация атрибутов класса
        """

        self.__language = 'EN'

    @property
    def language(self):
        """
        Защита от изменения в ручную языка раскладки
        """

        return self.__language

    def change_lang(self):
        """
        Смена языка раскладки при вызове метода
        """

        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard (Item, Mixin_change_lang):
    """
    Товар: Клавиатура
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализация атрибутов класса - наследование атрибутов
        """

        super().__init__(name, price, quantity)
