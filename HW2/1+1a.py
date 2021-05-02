# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} like eating delicious food')

    def sleep(self):
        print(f'{self.name} need to sleep a little bit')


class Frog (Animal):
    def frog_skill (self):
        print(f'{self.name} can jump')


class Zebra(Animal):
    def zebra_skill (self):
        print(f'{self.name} can run')


class Bird(Animal):
    def bird_skill (self):
        print(f'{self.name} can fly')


class Elephant(Animal):
    def elephant_skill (self):
        print(f'{self.name} have a trunk')


class Lemur(Animal):
    def lemur_skill (self):
        print(f'{self.name} can climb trees')


frog = Frog('Frog')
zebra = Zebra('Zebra')
bird = Bird('Bird')
elephant = Elephant('Elephant')
lemur = Lemur('Lemur')


frog.frog_skill()
zebra.zebra_skill()
bird.bird_skill()
elephant.elephant_skill()
lemur.lemur_skill()

frog.eat()
frog.sleep()

for item in (frog,zebra,bird,elephant,lemur):
    instance = f'{isinstance(item,Animal)}'
    print(str(item.name) + ' is an instance of the Animals class: ' + instance)


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 # create an instance of Centaur class and call the common method of these classes and unique.



class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} like eating something special')

    def sleep(self):
        print(f'{self.name} need to sleep, sometimes')

    def study(self):
        print(f'{self.name} need studying everyday')

    def work(self):
        print(f'{self.name} need to work, if she want to earn some money')



class Centaur (Human, Animal):


    def home (self):
        print(f'{self.name} usually live in forest')

    def sleep(self):
         Human.sleep(self)


centaur = Centaur('Centaur')
print('---------------------------------------------------')
centaur.home()
centaur.sleep()