# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Shirley', 12)
cat2 = Cat('Willy', 3)
cat3 = Cat('Burrows', 17)


# 2 Create a function that finds the oldest cat
cats = [cat1, cat2, cat3]
print(cat1.age)

def oldest(cats):
    ages=[]
    for i in cats:
        catage = i.age
        ages.append(catage)
    #print(f'The oldest cat is {max(ages)}')
    return(max(ages))



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest(cats)} years old')
