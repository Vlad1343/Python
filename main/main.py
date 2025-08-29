## TURTLE --------------------------------------------------------------------------------------------------------------

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


## №1
# a1 = int(input('Введіть перше число: '))
# a2 = int(input('Введіть друге число: '))
# a3 = int(input('Введіть третє число: '))
# suma = a1+a2+a3
# proiz = a1*a2*a3
# print('Сума чисел:',suma)
# print('Добуток чисел:',proiz)


## №2
# a1 = int(input('Введіть перше число: '))
# a2 = int(input('Введіть друге число: '))
# a3 = int(input('Введіть третє число: '))
# max_num = max(a1, a2, a3)
# min_num = min(a1, a2, a3)
# average_num = (a1 + a2 + a3) / 3
# print('Найбільше число:',max_num)
# print('Найменше число:',min_num)
# print('Середнє арифметичне число:',average_num)


## №3
# import math
# metr = int(input('Введіть кількість метрів: '))
# duym = metr*39.37
# myli = metr*0.000621
# yard = metr*1.094
# print(f'В {metr} метрах {duym} дюймів')
# print(f'В {metr} метрах {myli} миль')
# print(f'В {metr} метрах {yard} ярдів')


## №4
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


## №5
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


# # №6
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


# # №7
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


# # №8
# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#   if i < 5:
#     print(i)



# # №9
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




# # FUN  -----------------------------------------------------------------------------------------------------------------------

# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# import math
# a = float(input("Enter radius: "))
# b = a**2
# print(b*math.pi)

# a = input("Enter your full name: ")
# b = " ".join(reversed(a.split()))
# print(b)

# a = input("Enter comma-separated numbers: ")
# list = a.split(",") #defined separator
# tuple = tuple(list)
# print('List : ', list)
# print('Tuple : ', tuple)

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# from datetime import date
# a = date(2011, 7, 2)
# b = date(2014, 7, 11)
# c = b - a
# print(c.days, "days")


# number = int(input("Enter the Natural Number: "))
# for j in range(1, number+1):
#     a = []
#     for i in range(1, j+1):
#         print(i, sep=" ", end=" ")
#         if i < j:
#             print("+", sep=" ", end=" ")
#         a.append(i)
#     print("=", sum(a))
# print()






## STRING -----------------------------------------------------------------------------------------------------------------------

# first = "John"
# last = "Smith"
# msg = f"{first} [{last}] is a coder" #Formatted string
# print(msg)

# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("n"))
# print(course.replace("Python", "Java"))
# print("Python" in course)
# print(f"Python" in {course})
# print(f"Python" in f"{course}")

# x = 2.9
# print(round(x))
# print(abs(-2.9))

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))


# print('65+279=', 65 + 279)
# print('21*15=', 21 * 15)
# print('Програма завершена')
# input()

# name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
# print("\n")
# print("User Details: ", name, age, marks)

# a_1, *a_2, a_3 = (1,6,2,3,4,5)
# print(a_1, *a_2, a_3)

# a = (100,61,55)
# print(a)

# x = [1,2,3]
# y = x.copy()
# x.append(4)
# print(y)

# a = [1, 2, 3]
# b = ['x', 'y']
# c = [True, False, True, False]
# result = list(zip(a, b, c))
# print(result)

# values = [0, '', [], (), False, None, 'Non-empty string']
# result = any (values)
# print(result)

# print([*filter(lambda x: x % 3 == 2, {11, 11, 17, 21})])

# a = ["a", "c"]
# print([*enumerate(a)])

# n1 = 400_000_000
# n2 = 5_000
# result = n1*n2
# print(f"{result:,}")

# try:
#   print(eval("2+3"))
# except:
#   print("Error")

# a = int(input("Your phone number: "))
# b = sum([int(i) for i in str(a)])
# print(b)
# b = sum(list(map(int, str(a))))
# print(b)


# course = "Python for begginers"
# print(course.find("h"))


# n: int = 1000000000
# print(f"{n:,}")

# var: str = "Vlad Shutkevych"
# print(f"{var:>20}:")
# print(f"{var:20}:")
# print(f"{var:^20}:")
# print(f"{var:-^21}:")

# from datetime import datetime
# now: datetime = datetime.now()            #same as now = datetime.now()
# print(f"{now:%d.%m.%y [%H:%M:%S]}")
# print(f"{now:%c}")
# print(f"{now:%I%p}")

# n: float = 1234.5678
# print(round(n, 2))
# print(f"Result: {n:.2f}")
# print(f"Result: {n:,.2f}")

# a = 5
# b = 10
# var = "Bob says hi"
# print(f"a + b = {a+b}")
# print(f"{a + b = }")
# print(f"{bool(a) = }")



# name = input("What's your name? ").title().strip()

# name = name.strip()
# name = name.capitalize()

# name = name.title().strip()

# first, last = name.split(" ")
# print(f"Hello, {first}!")



# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = round(x + y, 3)
# print(f"{z:,}")



# print("meow\n" * 3, end="")



# def main():
#   phone = "617-495-1000"
#   print(phone[0:3])
#   print(phone[-4:])
  

# main()









## EXCEPTIONS -----------------------------------------------------------------------------------------------------------------------



# try:
#   age = int(input("Age: "))
#   income = 20_000
#   risk = income / age
#   print(age)
# except ValueError:
#   print("Invalid value")
# except ZeroDivisionError:
#   print("Invalid number")
  


# def func():
#   try:
#     raise ValueError("Bad value")
#   except ValueError:
#     # print("An error occurred")
#     return 1
#   finally:
#     # print("Finally block executed")
#     return 0

# print(func())



# try:
#   x = int(input("What's x? "))
# except ValueError:
#   print("Invalid value")
# else:
#   print(f"x is {x}")




# while True:
#   try:
#     x = int(input("What's x? "))
#   except ValueError:
#     print("Invalid value")
#   else:
#     break

# print(f"x is {x}")




# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x


# main()





# def main():
#     x = get_int("What's x? ")
#     print(f"x is {x}")


# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass


# main()





# def main():
#   pace = get_pace(miles=26.2, minutes=180)
#   print(f"You need to run each mile in {round(pace, 2)} minutes.")

# def get_pace(miles, minutes):
#   return minutes / miles

# main()





## VALUES -----------------------------------------------------------------------------------------------------------------------

# import random                        #import random as rand
# for i in range(3):
#   print(random.random())
#   print(random.randint(10, 20))

# members = ["John", "Mary", "Bob", "Mosh"]
# leader = random.choice(members)
# print(leader)

# v = 257
# y = 257
# print(v == y)  # True (values are equal)
# print(v is y)  # Might be True or False depending on the environment
# print(id(v))   # Memory address of v
# print(id(y))   # Memory address of y







## Walrus operator ----------------------------------------------------------------------------------------


list = [1, 2, 3]
if n := len(list) > 1:
    print(f"List has to much elements")











