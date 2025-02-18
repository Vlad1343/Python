# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def greet(self):
#     print(f"My name is {self.name}")
#     return(f"I am {self.age} years old")
# person1 = Person("Alice", 30)
# print(person1.greet())


# class Dog:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#   def sit(self):
#     print(f'{self.name} is now sitting.')
#   def roll_over(self):
#     print(f'{self.name} rolled over')
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 5)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()
# your_dog.sit()


# class ElectricCar(Car):
#   def __init__(self,make,model,year):
#     super().__init__(make,model,year)
# my_tesla = ElectricCar('tesla','model s', 2019)
# print(my_tesla.get_descriptive_name())



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
        
#     def draw(self):
#         print("Draw")


# point1 = Point()
# point1.draw()
# point2 = Point()
# point2.x = 10
# print(point2.x)

# point = Point(10, 20)
# point.x = 11
# print(point.x)



# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hello, I am {self.name}")
    
        
# john = Person("John Smith")
# john.talk()

# bob = Person("Bob Marley")
# bob.talk()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person("Alice", 25)
# print(person1.name)
# print(person1.age)



# class VirtualPet:
#     color = "brown"
#     legs = 4
#     lives = 9
# fluffy = VirtualPet()    #fluffy - instance; VirtualPet - definition
# print(fluffy.color)



# class Microwave:
#     def __init__(self, brand: str, power_rating: str):
#         self.brand = brand
#         self.power_rating = power_rating

# smeg = Microwave("Smeg", "B")
# print(smeg.brand, smeg.power_rating)      #self refers to every instance e.g. smeg and bosh
# bosch = Microwave("Bosch", "C")
# print(bosch.brand, bosch.power_rating)        




# class Microwave:
#     def __init__(self, brand: str, power_rating: str):
#         self.brand = brand
#         self.power_rating = power_rating
#         self.turned_on = False
        
#     def turn_on(self):
#         if self.turned_on:
#             print(f"Microwave ({self.brand}) is already turned on")
#         else:
#             self.turned_on = True
#             print(f"Microwave ({self.brand}) is now turned on")       
            
#     def turn_off(self):
#         if self.turned_on:
#             self.turned_on = False
#             print(f"Microwave ({self.brand}) is now turned off")
#         else:
#             print(f"Microwave ({self.brand}) is already turned off")
            
#     def run(self, seconds):
#         if self.turned_on:
#             print(f"Running ({self.brand}) for {seconds} seconds")
#         else:
#             print(f"Turn on your microwave first")
            
#     def __add__(self, other):           #dunder method (two underscores) / magic methods
#         return f"{self.brand} + {other.brand}"
    
#     def __mul__(self, other):
#         return f"{self.brand} * {other.brand}"
    
#     def __str__(self): 
#         return f"Microwave({self.brand}), Rating: {self.power_rating}"
    
#     def __repr__(self):
#         return f"REPR"
        
# smeg = Microwave("Smeg", "B")
# bosch = Microwave("Bodch", "C")
# smeg.turn_on()
# smeg.turn_on()
# smeg.run(10)
# smeg.turn_off()
# smeg.run(10)
# print(smeg + bosch)
# print(smeg * bosch)
# print(smeg)
# print(bosch)
# print(repr(smeg))      #__repr__ method is called when you want to see a string representation of the object
            




# # INHERITANCE --------------------------------------------------------------------------------------------------------------------------------


# class Mammal:
#     def walk(self):
#         print("Walk")
        
        
# class Dog(Mammal):
#     def bark(self):
#         print("Bark")

# class Cat(Mammal):
#     pass


# dog1 = Dog()
# dog1.walk()
# dog1.bark()



## MODULES --------------------------------------------------------------------------------------------------------------------------------

# from utils import find_max       #go to utils.py
# numbers = [10, 3, 6, 15]
# max = find_max(numbers)
# print(max(numbers))


# from ecommerce import shipping
# shipping.calc_shipping()



## PACKAGES --------------------------------------------------------------------------------------------------------------------------------
#
# import random
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())


# from pathlib import Path
# path = Path("ecommerce")
# print(path.exists())
# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

# path = Path()
# for file in path.glob("*"):              #*.* / *.py / *
#     print(file)                          #PyCharm