from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def add(self,other):
        if not isinstance(other,Item):
            raise ValueError
        return self.phone1 + other.item1


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim, number):
        if number <= 0:
            raise ValueError ("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = int(number)


