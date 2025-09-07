## Global variables -------------------------------------------------------------------




# balance = 0
# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(amount):
#     global balance
#     balance += amount

# def withdraw(amount):
#     global balance
#     balance -= amount
    
# if __name__ == "__main__":
#     main()




# class Account:
#     def __init__(self):
#         self._balance = 0
    
#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         self._balance += amount
    
#     def withdraw(self, amount):
#         self._balance -= amount
    
# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance:", account.balance)

# if __name__ == "__main__":
#     main()
        
        
   
        


## Constants -------------------------------------------------------------------------------


# MEOWS = 3        
# for _ in range(MEOWS):
#     print("Hello")



# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("Meow")

# cat = Cat()
# cat.meow()






## Type Hints and Docstrings -------------------------------------------------------------------


# def meow(n: int):
#     for _ in range(n):
#         print("Meow")           #use mypy to check type hints

# number: int = int(input("Number: "))
# meow(number)



# def meow(n: int) -> str:
#     """
#         Prints 'Meow' n times.
#         :param n: Number of times to print 'Meow'
#         :type n: int
#         :raise TypeError: If n is not an int
#         return: A string with 'Meow' n times
#         :rtype: str (return type)
#     """
#     return "Meow\n" * n       

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")






## Argparse -------------------------------------------------------------------------------

# import sys
# if len(sys.argv) == 1:
#     print("Meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("Meow")
# else:
#     print("Usage: etc.py [-n <number>]")



# import argparse      #argument parser
# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()
# for _ in range(int(args.n)):
#     print("meow")
    

# import argparse
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args()
# for _ in range(int(args.n)):        #python3 etc.py -h
#     print("meow")                   #python3 etc.py --help



# import argparse
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args()
# for _ in range(args.n):
#     print("meow")



## Unpacking -------------------------------------------------------------------------------


# first, last = input("Enter your name: ").split(" ")
# print(f"Hello, {first} {last}")



# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# print(total(100, 50, 25), "Knuts")
    
    
    

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "Knuts")




# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
# print(total(*coins), "Knuts")



# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(**coins), "Knuts")  #unpacking a dictionary
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")






## Args & Kwargs --------------------------------------------------------------------------------

# args(arguements) & kwargs(keyword agruements) are used to pass a variable number of arguments to a function
# args are positional arguments, such as those we provide to print like print("Hello", "World").
# kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").
# args are passed as a tuple, while kwargs are passed as a dictionary.


# def f(*args, **kwargs):
#     print("Positional", args)

# f(100, 50, 25, 5)



# def f(*args, **kwargs):
#     print("Named", kwargs)

# f(galleons=100, sickles=50, knuts=25)




## Map and Filter --------------------------------------------------------------------------------

# map is used to apply a function to every item in an iterable (like a list) and return a new iterable with the results.
# filter is used to filter items in an iterable based on a function that returns True or False.



# def main():
#     yell("This is a test")

# def yell(phrase):
#     print(phrase.upper())

# if __name__ == "__main__":
#     main()
    
    
    
    
# def main():
#     yell(["This", "is", "CS50"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()




# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)


# if __name__ == "__main__":
#     main()




# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.upper, words)    #map(function, iterable)
#     print(*uppercased)

# if __name__ == "__main__":
#     main()



# arr1 = [1, 2, 3, 4, 5]
# arr2 = map(lambda x: 2 * x, arr1)
# print(list(arr2))


# from functools import reduce
# arr1 = [1, 2, 3, 4, 5]
# arr2 = reduce(lambda x,y: x+y, arr1)
# print(arr2)  
# #reduce(function, iterable) applies the function cumulatively to the 
# #items of the iterable, reducing it to a single value.


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])





## List Comprehensions ---------------------------------------------------------------------


# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = [word.upper() for word in words]  #list comprehension
#     print(*uppercased)

# if __name__ == "__main__":
#     main()




# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])
##or
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)





## Dictionary Comprehensions ---------------------------------------------------------------------


# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
# #or
# gryffindors = [
#     {"name": student, "house": "Gryffindor"} for student in students
# ]
# #or
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)



 
## Enumerate --------------------------------------------------------------------------------


# students = ["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i + 1, students[i])
    
    
# students = ["Hermione", "Harry", "Ron"]
# for i, student in enumerate(students):
#     print(i + 1, student)





## Generators and Iterators--------------------------------------------------------------------------------


# n = int(input("What's n? "))
# for i in range(n):
#     print("🐑" * i)


# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print("🐑" * i)

# if __name__ == "__main__":
#     main()



# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print(sheep(i))

# def sheep(n):
#     return "🐑" * n

# if __name__ == "__main__":
#     main()



# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

# if __name__ == "__main__":
#     main()




# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     for i in range(n):
#         yield "🐑" * i

# if __name__ == "__main__":
#     main()



## String Formatting -------------------------------------------------------------------------------

## %s - String (or any object with a string representation, like numbers)
## %d - Integers
## %f - Floating point numbers
## %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
## %x/%X - Integers in hex representation (lowercase/uppercase)


# name = "John"
# print("Hello, %s!" % name)


# name = "John"
# age = 23
# print("%s is %d years old." % (name, age))


# mylist = [1,2,3]
# print("A list: %s" % mylist)


# data = ("John", "Doe", 53.44)
# format_string = "Hello"
# print("%s %s %s. Your current balance is $%.2f."% (format_string, data[0], data[1], data[2]))





##General --------------------------------------------------------------------------------

# import re
# find_members = dir(re)
# for member in find_members:
#     if "find" in member:
#         print(member)
        
        
# import re
# find_members = []
# for member in dir(re):
#     if "find" in member:
#         find_members.append(member)

# print(sorted(find_members))



# a = [1, 2, 3, 2, 1]
# b = [3, 2, 2, 3, 3, 2]

# uniq = []
# for i in a:
#     if i not in uniq:
#         uniq.append(i)
# for i in b:
#     if i not in uniq:
#         uniq.append(i)
# print(uniq)



# a = [1, 2, 3, 2, 1]
# b = [3, 2, 2, 3, 3, 2]
# print(list(set(a) | set(b)))



# lst = [1, 2, 3, 2, 4, 5, 1, 6]
# duplicates = []
# for x in lst:
#     if lst.count(x) > 1 and x not in duplicates:
#         duplicates.append(x)
# print(duplicates)



# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# duplicates = list(set(a) & set(b))  # & is intersection
# print(duplicates)



# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# duplicates = []
# for x in a:
#     if x in b and x not in duplicates:
#         duplicates.append(x)
# print(duplicates)


## Escape Characters -------------------------------------------------------------------------------

# print('She said, "It\'s a beautiful day!"')
# print("She said, \"It's a beautiful day!\"")
# print("Hi, how are you?\nI'm great!")
# print("Here's a backslash: \\")



## Time Module -------------------------------------------------------------------------------


# import time
# import sys

# sys.set_int_max_str_digits(0)
# def calcProd():
#  # Calculate the product of the first 100,000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product
# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))





import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
time.sleep(6)