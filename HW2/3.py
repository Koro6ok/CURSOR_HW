# Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
# Override a printable string representation of Profile class and return: list of the params mentioned above

class Worker:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

        self.worker_profile = [self.name, self.last_name, self.phone_number, self. address, self.email, self.birthday, self.age, self.sex]


    def __str__(self):
        return (f'{self.name}, you enter the information below, into you profile: \n{self.worker_profile}')


worker = Worker('Yana', 'Tural', '8-800-555-35-35', 'Kyiv, Ukr', 'yanatural@gmail.com', '00.00.0000', "2021", 'male')

print(worker)