from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Информация по классу для разработчика
        """

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Информация по классу для пользователя
        """

        return self.name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """
        После изменения значения количества сим-карт, проверяем, чтобы число было больше нуля и было целым числом
        """

        if num > 0 and type(num) == int:
            self.__number_of_sim = num
        else:
            print('Ошибка: Количество физических SIM-карт должно быть целым числом больше нуля.')
