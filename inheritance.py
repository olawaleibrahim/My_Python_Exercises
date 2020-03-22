class User:
    def sign_in(self, age):
        while age <= 10:
            break
        else:
            print('You are signed in')


class Wizard(User):  # creating a subclass to inherit the properties of the User class
    def __init__(self, _name, _power):
        self._name = _name
        self._power = _power

    def attack(self):
        print(f'{self._name} is attacking with a power of {self._power} Amperes')
        return 'done'


class Archer(User):  # creating a subclass to inherit the properties of the User class
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} is attacking with a number of {self.arrows} arrows')
        return 'done'


wizard1 = Wizard('Merlin', 200)
archer1 = Archer('Oliver', 9)

print(wizard1.attack())
print(archer1.attack())

# print(archer1.sign_in(12))

print(isinstance(archer1, Archer))

wizard1.attack = 'David'
print(wizard1.attack)
