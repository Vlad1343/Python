
# Object-Oriented Programming (OOP)
# OOP is a programming paradigm that uses objects and classes to structure code.


# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()





# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()





# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()






# class Student:
#     def __init__(self, name, house):    
#         self.name = name     #attribute/property
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)     #object/instance
#     return student                     #name, house - instance attributes

# if __name__ == "__main__":
#     main()





# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()





# class Student:
#     def __init__(self, name, house, patronus=None):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
#             raise ValueError("Invalid patronus")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶"
#             case _:
#                 return "🪄"

# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ") or None
#     return Student(name, house, patronus)

# if __name__ == "__main__":
#     main()





# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Invalid name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

# def main():
#     student = get_student()
#     student.house = "Number Four, Privet Drive"
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()






# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Invalid name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # Getter for house - function for a class that gets some attributes
#     @property
#     def house(self):
#         return self._house

#     # Setter for house - function in some class that sets some value.
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()







# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # Getter for name
#     @property
#     def name(self):
#         return self._name

#     # Setter for name
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Invalid name")
#         self._name = name

#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()










# import random
# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()         #Instantiating - creating a new object from a class
# hat.sort("Harry")


# import random
# class Hat:

#     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     @classmethod #class method - method that is bound to the class and not the instance of the class
#     def sort(cls, name): #cls - class itself
#         print(name, "is in", random.choice(cls.houses))

# Hat.sort("Harry")





# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)

# def main():
#     student = Student.get()
#     print(student)

# if __name__ == "__main__":
#     main()





# import time
# def tiktok(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         t2 = time.time() - t1
#         print(f"Time taken: {t2:.2f} seconds")
#     return wrapper

# @tiktok
# def do_this():
#     time.sleep(2)
    
# @tiktok
# def do_that():
#     time.sleep(.3)

# do_this()
# do_that()
# print("Done")






# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts

#     def __str__(self):
#         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

#     def __add__(self, other):
#         galleons = self.galleons + other.galleons
#         sickles = self.sickles + other.sickles
#         knuts = self.knuts + other.knuts
#         return Vault(galleons, sickles, knuts)

# potter = Vault(100, 50, 25)
# print(potter)

# weasley = Vault(25, 50, 100)
# print(weasley)

# total = potter + weasley
# print(total)






# class Food:
#     base_hearts = 1
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         self.hearts = Food.calculate_hearts(ingredients)
    
#     @classmethod
#     def calculate_hearts(cls, ingredients):
#         hearts = cls.base_hearts
#         for ingredient in ingredients:
#             if "hearty" in ingredient.lower():
#                 hearts += 2
#             else:
#                 hearts += 1
#         return hearts
    
#     @classmethod
#     def from_nothing(cls, hearts):
#         food = cls(ingredients=[])
#         food.hearts = hearts
#         return food

# def main():
#     mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
#     print(f"This skewer heals {mushroom_skewer.hearts} hearts")
#     mushroom_skewer = Food.from_nothing(hearts=2)
#     print(f"This skewer heals {mushroom_skewer.hearts} hearts")
    
# main()





# class Package:
#     def __init__(self, number, sender, recipient, weight):
#         self.number = number
#         self.sender = sender
#         self.recipient = recipient
#         self.weight = weight

#     def __str__(self):
#         return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg;"

#     def calculate_cost(self, cost_per_kg):
#         return self.weight * cost_per_kg
        
# def main():
#     packages = [
#         Package(1, "Alice", "Bob", 2.5),
#         Package(2, "Charlie", "Dave", 1.0),
#         Package(3, "Eve", "Frank", 3.2)
#     ]
#     for package in packages:
#         print(f"{package} costs £{package.calculate_cost(cost_per_kg=2)}")
            
# if __name__ == "__main__":
#     main()




# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# miles = Dog("Miles", 4)
# print(miles.description())
# print(miles.speak("Woof Woof"))
# print(miles.speak("Bow Wow"))




# class Parent:
#     speaks = ["English"]

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.speaks.append("German")




# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
# print(miles)
# print(buddy.speak("Woof Woof"))
# print(isinstance(miles, Dog))




# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"
#         return super().speak(sound)
    
# miles = JackRussellTerrier("Miles", 4)
# print(miles.speak())




# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# class GoldenRetriever(Dog):
#     def speak(self, sound="Arf"):
#         return super().speak(sound)



