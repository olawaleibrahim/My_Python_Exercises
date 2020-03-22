class MyObject:  # class created(blueprint)
    pass


obj1 = MyObject()  # an instance of the class created(object/instance of the class)
print(type(obj1))


class PlayerCharacter:  # class created
    existence = True  # class object attribute

    def __init__(self, name = 'anonymous', age = 19):  # name, age are attributes of the class
        if (age > 18):
            self.name = str(name)
            self.age = int(age)

    def shout(self):
        print(f'My name is {self.name} and I am {self.age} years old')
        return 'done'

    def run(self):
        print("Run away")


player1 = PlayerCharacter('Shepherd', 32)  # class initiated, object created
player2 = PlayerCharacter('Witcher')
print(player2.name)
print(player1.age)
print(player2.age)

print(player1.shout())
print(player2.shout())

print('\n')

player1.money = 500

print(player1.money)


print(player1.existence)
