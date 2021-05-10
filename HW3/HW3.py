from abc import ABC, abstractmethod
import random


class HumanMain(ABC):
    def __init__(self, name: str, age: int, available_money: (int,float), own_house: list = []):
        self.name = name
        self.age = age
        self.available_money = available_money
        self.own_house = own_house

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self, salary):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Person(HumanMain):
    def __init__(self, name, age, available_money, own_house):
        super().__init__(name, age, available_money, own_house)


    def info(self):
        print(f'Person info:\n'
              f'name - {self.name}\n'
              f'age - {self.age}\n'
              f'available money - {self.available_money}\n'
              f'own_house {self.own_house}')

    def make_money(self, salary):
        # множу на 0.2 (бо інтернет каже, що потрібно відкладати 20% від зарплати)
        earn = salary*0.2
        self.available_money += earn
        print (f'{self.name} can make {earn} every month and in this month he has {self.available_money}')
        return self.available_money

    def buy_house(self, house):
        if self.available_money >= house.cost:
            self.available_money -= house.cost
            self.own_house.append(house)
            print(f'{self.name} bought a house')
        else:
            print(f'{self.name} hasn`t enough money to buy a house')
        return tuple(self.own_house)


class House(ABC):
    def __init__(self, cost: (float, int), area: (float, int)):
        self.cost = cost
        self.area = area


class Obj_house(House):
    def __init__(self, cost, area):
        super().__init__(cost, area)

    def discount(self, disc):
        self.cost -= self.cost*disc
        return self.cost



class RieltorMain(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Rieltor(metaclass=RieltorMain):
    def __init__(self, name:str, give_discount: (float, int), av_houses: list = []):
        self.name = name
        self.give_discount = give_discount
        self.av_houses = av_houses

    def give_info(self):
        if self.av_houses is not None:
            print(f'Now, {self.name} can show and sell the following houses (cost, area):')
            for dom in self.av_houses:
                print(f'{dom.cost}, {dom.area}')
        else:
            print(f'Sorry, but rieltor {self.name} can`t propose you a house')


    def discount(self):
        return self.give_discount


    def steal_money(self):
        if random.randint(0, 10) == 10:
            print(f'Rieltol {self.name} stolen your money')


if __name__ == '__main__':
    house1 = House(30000, 40)
    house2 = House(65000, 80)
    house3 = House(150000, 140)



person1 = Person('Buyer', 69, 100000, [])
person1.info()
person1.make_money(1500)

print('-----------------------------------------------------')

realtor = Rieltor('Rieltor', 0.4, [house1, house2, house3])
realtor.give_info()
realtor.discount()
realtor.steal_money()

print('-----------------------------------------------------')

person1.buy_house(house1)
person1.buy_house(house2)
person1.buy_house(house3)




