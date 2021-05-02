# 2.a  Make the class with composition.

class MyPhone:
    def __init__(self, mobile):
        self.mobile = mobile


class CellPhone:
    def __init__(self):
        phone_mark = MyPhone('Xiaomi - is mark/brand of my phone')
        phone_os = MyPhone('Android - is operation system of my phone')
        self.mobile = [phone_mark, phone_os]


person_phone = CellPhone()

for phone in person_phone.mobile:
    print(phone.mobile)

print('-----------------------------------------')



# 2.b  Make the class with aggregation.

class Person:
    def __init__(self, age):
        self.age = age


class Age_type:
    def __init__(self, age_class):
        self.age_class=age_class

age_years = Age_type (21)
this_person = Person(age_years)


if  0 < this_person.age.age_class < 15:
    print('Given a person`s age, I can say that she is children and young person')
elif 15 <= this_person.age.age_class < 65:
    print('Given a person`s age, I can say that she is youth and adults')
elif this_person.age.age_class >= 65:
    print('Given a person`s age, I can say that she is the elderly')