# a = int(input('Введіть годину дня: '))
# if a>=6 and a<=12:
#    print('Ранок')
# elif a>=13 and a<=18:
#   print('День')
# elif a>=19 and a<=23:
#   print('Вечір')
# elif a==24:
#   print('Ніч')
# elif a>=1 and a<=5:
#   print('Ніч')
# else:
#   print('Помилка')


# import this

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[-1])
# message = f'My first bicycle was a {bicycles[0].title()}.'
# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati'
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles.insert(1, 'ducati')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# motorcycles.remove('honda')
# print(motorcycles)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))
# cars.reverse()
# print(cars)
# len(cars)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#   # print(magician)
#   print(f'{magician.title()}, that was a great trick!')

# for value in range(1,5):
#   print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#   square = value**2
#   squares.append(square)
# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# a = min(digits)
# print(a)
# b = max(digits)
# print(b)
# c = sum(digits)
# print(c)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])
# for dimension in dimensions:
#   print(dimension)

# alien_0 = {'color': 'green', 'points' : 5}
# print(alien_0['color'])
# alien_0['color']='yellow'
# del alien_0['points']
# print(alien_0)
# points_value = alien_0.get('points', 'No point value assigned')
# print(points_value)

# user_0 = {
#   'username': 'efermi',
#   'first': 'enrico',
#   'last': 'fermi',
# }

# for key, value in user_0.items():
#   print(f'\nKey: {key}')
#   print(f'Value: {value}')

# for key in user_0.keys():
#   print(key.title())

# for key in sorted(user_0.keys()):
#   print(f'{key.title()}, thank you')

# for key in user_0.values():
#   print(key.title())

# for key in set(user_0.keys()):
#   print(key.title())

# aliens = []
# for alien_number in range(30):
#   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#   aliens.append(new_alien)
# for alien in aliens[:5]:
#   if alien['color'] == 'green':
#     alien['color'] = 'yellow'
#     alien['speed'] = 'medium'
#     alien['points'] = 10
# for alien in aliens[:5]:
#   print(alien)

# def greet_user():
#   print('Hello')
# greet_user()

# def greet_user(username):
#   print(f'Hello, {username.title()}!')
# greet_user('vlad')

# def pet(type, name):
#   print(f'\nI have a {type}.')
#   print(f"My {type}'s name is {name.title()}.")

# pet('dog', 'Jack')

# def pet(type, name):
#   print(f'\nI have a {type}.')
#   print(f"My {type}'s name is {name.title()}.")

# pet(type='dog', name='Jack')



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

# import turtle
# window = turtle.Screen()
# turtle.reset()
# turtle.shape('turtle')
# turtle.bgcolor('black')
# turtle.color('white')
# turtle.speed(15)
# turtle.pensize(3)
# for i in range(40):
  # turtle.left(45)
  # turtle.forward(40)
  # turtle.left(90)
  # turtle.forward(40)
  # turtle.left(50)
  # turtle.forward(70)
  # turtle.left(90)
  # turtle.forward(90)
  # turtle.left(30)
  # turtle.penup()
  # turtle.forward(30)
  # turtle.right(50)
  # turtle.circle(40)
  # turtle.pendown()

  # turtle.circle(5*i)
  # turtle.circle(-5*i)
  # turtle.left(i)





# # №1
# a1 = int(input('Введіть перше число: '))
# a2 = int(input('Введіть друге число: '))
# a3 = int(input('Введіть третє число: '))
# suma = a1+a2+a3
# proiz = a1*a2*a3
# print('Сума чисел:',suma)
# print('Добуток чисел:',proiz)


# # №2
# a1 = int(input('Введіть перше число: '))
# a2 = int(input('Введіть друге число: '))
# a3 = int(input('Введіть третє число: '))
# max_num = max(a1, a2, a3)
# min_num = min(a1, a2, a3)
# average_num = (a1 + a2 + a3) / 3
# print('Найбільше число:',max_num)
# print('Найменше число:',min_num)
# print('Середнє арифметичне число:',average_num)


# №3
# import math
# metr = int(input('Введіть кількість метрів: '))
# duym = metr*39.37
# myli = metr*0.000621
# yard = metr*1.094
# print(f'В {metr} метрах {duym} дюймів')
# print(f'В {metr} метрах {myli} миль')
# print(f'В {metr} метрах {yard} ярдів')


# №4
# num = input('Введіть число від 1 до 100: ')
# if num.isdigit():
#   num = int(num)
#   if 1 <= num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#       print('Fizz Buzz')
#     elif num % 3 == 0:
#       print('Fizz')
#     elif num % 5 == 0:
#       print('Buzz')
#     else:
#       print(num)
#   else:
#     print('Помилка! Число не знаходиться в діапазоні від 1 до 100')
# else:
#   print('Помилка! Це не число')


# №5
# num = input('Введіть число: ')
# if num.isdigit():
#   num = int(num)
#   print('Виберіть степінь від 0 до 7: ')
#   stepen = input()
#   if stepen.isdigit():
#     stepen = int(stepen)
#     if 0 <= stepen <= 7:
#       res = num**stepen
#       print(f'{num} в степені {stepen} дорівнює {res}')
#     else:
#       print('Помилка! Ви вибрали не той степінь')
#   else:
#     print('Помилка! Ви ввели не число')
# else:
#   print('Помилка! Ви ввели не число')


# №6
# cost = float(input('Введіть вартість розмови: '))
# operator = {
#   'Kyivstar': 4.0,
#   'Vodafone': 4.5,
#   'Lifecell': 5.0,
# }
# print('Виберіть оператора: ')
# for i in operator:
#   print(operator)
# select = input()
# if select in operator:
#   tarif = operator[select]
#   call = cost * tarif
#   print('Вартість дзвінка:', call)
# else:
#   print('Оператора не знайдено')


# №7
# import turtle
# window = turtle.Screen()
# turtle.reset()
# turtle.shape('turtle')
# turtle.bgcolor('gray')
# turtle.color('blue')
# turtle.speed(15)
# turtle.pensize(3)
# for i in range(40):
#   turtle.left(35)
#   turtle.forward(75)
#   turtle.left(75)
#   turtle.forward(75)
#   turtle.left(50)
#   turtle.forward(35)
#   turtle.left(75)
#   turtle.forward(65)
#   turtle.left(20)


# №8
# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#   if i < 5:
#     print(i)



# №9
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# aa = set(a)
# bb = set(b)
# element = list(aa.intersection(bb))
# print(element)
    


# # №10
# chocko = int(input('Скільки грам карамелі Ви хочете купити? '))
# a = 270
# n = a*chocko/1000
# if chocko < 500:
#   print(f'Сума до сплати: {n}')
# if chocko > 500:
#   a = 200
#   n = a*chocko/1000
#   print(f'Сума до сплати: {n}')


# print('65+279=', 65 + 279)
# print('21*15=', 21 * 15)
# print('Програма завершена')
# input()

# import random

# def guess_number_game():
#     print("Welcome to the Number Guessing Game!")
#     number_to_guess = random.randint(1, 100)
    
#     while True:
#         user_guess = input("Guess a number between 1 and 100: ")
#         if user_guess.isdigit():
#             guess = int(user_guess)
#             if guess == number_to_guess:
#                 print("Congratulations! You've guessed the correct number!")
#                 break
#             elif guess < number_to_guess:
#                 print("The number is higher. Try again.")
#             else:
#                 print("The number is lower. Try again.")
#         else:
#             print("Please enter a valid number.")

# guess_number_game()

# a_1, *a_2, a_3 = (1,6,2,3,4,5)
# print(a_1, *a_2, a_3)

# a = (100,61,55)
# print(a)
