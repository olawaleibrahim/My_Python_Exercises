class Player:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def DisplayProfile(self):
        if self._age > 11:
            print(
                f'Welcome... \n Your name is {self._name} and you are {self._age} years old')
        
        else:
            print(
                f'You are not of age'
            )
        return 'done'


player1 = Player('Beckham', 20)
player2 = Player('Marie', 17)


player1._name = 'Tunde'
player1._age = 18

print(player1.DisplayProfile())
