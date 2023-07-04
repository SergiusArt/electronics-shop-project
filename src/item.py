from csv import DictReader
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR_ITEMS = Path.joinpath(ROOT, 'src', 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        Информация по классу для разработчика
        """

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Информация по классу для пользователя
        """

        return self.__name

    @property
    def name(self):
        """
        Позволяет обращаться к имени как к аргументу
        """

        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Позволяет изменять имя и оставляет первые 10 символов
        """

        self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса данными из файла
        """
        cls.all = []
        with open(DIR_ITEMS, 'r', encoding='windows-1251') as csvfile:
            data = DictReader(csvfile)
            for item in data:
                cls(name=item['name'], price=cls.string_to_number(item['price']),
                    quantity=cls.string_to_number(item['quantity']))

    @staticmethod
    def string_to_number(str_num):
        """
        Возвращает число из числа-строки
        """

        return int(float(str_num))
