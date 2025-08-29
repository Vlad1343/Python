# def greet_user():
#   print("Hi there")          
#   print("Welcome on board")  

# greet_user()


# def square(number):
#   return number * number

# result = square(3)            #return gives a result back so you can use it later.
# print(result)                 #print just displays a value but doesn't return anything
# print(square(3))



# def emoji_converter(message):
#   words = message.split(" ")
#   emojis = {
#   ":)": "🙂",
#   ":(": "😕"
# }
#   output = ""
#   for word in words:
#     output += emojis.get(word, word) + " "
#     return output

# message = input("> ")
# print(emoji_converter(message))
  


# def greet_user(name, surname):                #parameters are the holes or placeholders that we define in our function for receiving info
#   print(f"{name} {surname}, welcome on board")
  
# greet_user("John", "Smith")                   #arguments are the actual pieces of info that we supply to these functions
# greet_user(surname = "Smith", name = "John")
# greet_user("Mary")


# def say_hi(self):
#   print(f"Hi, my name is {self}")
# say_hi("Vlad")

# def add_bonus(salary):
#   bonus = 100
#   print(salary+bonus)
# add_bonus(1900)

# def add_shipping(cart):
#   if cart < 100:
#     print(f"Total: {cart + 10}")
#   else:
#     print(f"Total: {cart}")
# add_shipping(45)
# add_shipping(200)

# def halve_prices(cart):
#   for price in cart:
#     print(f"New price: {price/2}")
# cart_list = [5, 20, 15]
# halve_prices(cart_list)

# def is_valid(parts):
#   print(len(parts) == 2)
# email = "vladshutkevych@gmail.com"
# user = email.split("@")
# is_valid(user)

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


# def display_programme(movies):
#   for i in movie_list:
#     print(f"Airing tonight: " + i)
# movie_list = ["Toy Story", "Thor"]
# display_programme(movie_list)


# def first(leader, player):
#   leader[0] = player
#   return leader
# leader = ["Jake", "Mike", "Kevin"]
# leader = first(leader, "Lena")
# print(leader)


# def passengers(booking):
#   counter = 1
#   while counter <= booking:
#     print(f"Passenger {counter} on board")
#     counter += 1
# passengers(4)


# def progress(files):
#   for i in range(files):
#     print(f"Downoading file {i} out of {files}")
# progress(3)

# def check_age(age):
#   can_drive = age >= 18
#   return age, can_drive
# print(check_age(17))


# def func(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
# result = func(20, 30)
# print("The result is", result)
# result = func(40, 30)
# print("The result is", result)


# prices = [10, 22, 30, 40, 58, 62]
# def halve(num):
#   no_tax = 0.85 * num
#   return num/2, no_tax/2
# halved = [halve(price) for price in prices]
# print(halved)

# authors = ["Virginia Woolf", "John Steinback"]
# def add_comma(name):
#   parts = name.split(" ")
#   return parts[1] + ", " + parts[0]
# authors_update = [add_comma(name) for name in authors]
# print(authors_update)



# def shipping(shipment):
#     return f"Shipping cost: {shipment * 1.2}"

# def calculate_total_cost(items, shipping_cost):
#     total = sum(items) + float(shipping_cost.split(': ')[1])
#     return total

# items = [10, 20, 30]
# shipping_cost = shipping(sum(items))
# total_cost = calculate_total_cost(items, shipping_cost)
# print(f"Total cost: {total_cost}")


# def double(num):
#     return num * 2

# numbers = [1, 2, 3, 4, 5]
# result = map(double, numbers)   #Applies double() to each item in numbers.
# print(list(result))



# def hello(to="World"):
#     print(f"Hello, {to}!")

# hello()
# name = input("What's your name? ")
# hello(name)



# def main():
#     name = input("What's your name? ")
#     hello(name)
#     hello()
# def hello(to="World"):
#     print("Hello,", to)

# main()



# def main():
#     x = int(input("What's x? "))
#     print("X squared is", square(x))

# def square(n):
#     return n*n #or n**2 or pow(n,2)

# main()


# def greet(input):
#     if "hello" in input:
#         return "Hello, there"
#     else:
#         return "Do not understand"
    
# z = greet("hello, computer")
# print(z + " Vlad")



# emoticon = "v.v"
# def main():
#     global emoticon
#     say("Is anyone there?")
#     emoticon = "XD"
#     say("Oh, hi!")
# def say(phrase):
#     print(phrase + " " + emoticon)

# main()



# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     return float(d.strip('$'))


# def percent_to_float(p):
#     return float(p.strip('%')) / 100



# def getTotal(a, b):
#     return a+b

# num1 = 3
# num2 = 5
# total = getTotal(num1, num2)
# print(total)




# def my_function(name):
#   print(name + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")



# def my_function(*kids):
#   print("The youngest child is " + kids[2])    #If you do not know how many arguments that will be passed 
                                                 #into your function, add a * before the parameter name in the function definition.

# my_function("Emil", "Tobias", "Linus")



# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)    

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# def my_function(**kid):
#   print("His last name is " + kid["lname"])          #If you do not know how many keyword arguments that will be passed into your function, 
#                                                       #add two asterisk: ** before the parameter name in the function definition.

# my_function(fname = "Tobias", lname = "Refsnes")




# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")




# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)




# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))



# def my_function(x, /):
#   print(x)

# my_function(3)




# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print("#" * (i+1))


# if __name__ == "__main__":
#     main()























#LAMBDA =================================================================================================

# #A lambda function is a small anonymous function (a function without a name).
## Syntax: lambda arguments : expression


# def add(x, y):
#     return x + y
# print(add(3, 5))

# #Same Thing with lambda

# add = lambda x, y: x + y
# print(add(3, 5))




# def square(n):
#     return n * n
# print(square(4))  

##Same Thing with lambda

# square = lambda n: n * n
# print(square(4))  



# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))



# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))





#RECURSION =================================================================================================


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)



# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)  #Recursion
#         elif item.is_a_key():
#             print("Found the key!")




# def countdown(i):
#     print (i)
#     if i <= 0:
#         return
#     else:
#         countdown(i-1)
# countdown(5)