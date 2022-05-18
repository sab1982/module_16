class Customers:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'''"{self.first_name} {self.last_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.first_name} {self.last_name}, г.{self.city}'


guest_1 = Customers('Иван','Иванов','Москва',50)
guest_2 = Customers('Владимир','Владимиров','Сочи',50)
guest_3 = Customers('Елена','Попова','Энгельс',50)

guest_list=[guest_1,guest_2,guest_3]


for guest in guest_list:
    print(guest.get_guest())