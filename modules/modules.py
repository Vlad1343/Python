
##RANDOM----------------------------------------------------------------------------------


# import random
# coin = random.choice(["heads", "tails"])
# print(coin)


# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)


# import random
# num = random.randint(1, 10)
# print(num)


# import random
# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for i in cards:
#     print(i)



# import random
# cards = ["jack", "queen", "king"]
# def main():
    # print(random.choices(cards, k=2))                        #with replacement
    # print(random.sample(cards, k=2))                         #without replacement
    # print(random.choices(cards, weights=[75,20,5], k=2))     #edit probabilities
    

# main()



# import random
# cards = ["jack", "queen", "king"]
# while True:
#     choose = random.choices(cards, weights=[75, 20, 1], k=1)
#     print(choose)
#     if "king" in choose:
#         break



# import random
# cards = ["jack", "queen", "king"]
# random.seed(1)
# print(random.choices(cards, k=2))                      

    

##STATISTICS----------------------------------------------------------------------------------


# import statistics
# print(statistics.mean([100, 90]))





##COMMAND-LINE ARGUMENTS----------------------------------------------------------------------------------------------------------


## python /Users/vladyslavshutkevych/Desktop/python/main/modules.py YourName


# import sys
# print("hello, my name is", sys.argv[1])   #argument vector



# import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
    
    
    
# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])



# import sys
# print(sys.version)


# import sys 
# for line in sys.stdin: 
# 	if 'q' == line.rstrip(): 
# 		break
# 	print(f'Input : {line}') 

# print("Exit") 



# import sys
# sys.stdout.write('Geeks')


# import sys 
# def print_to_stderr(*a): 
# 	print(*a, file = sys.stderr) 

# print_to_stderr("Hello World") 



# import sys
# n = len(sys.argv)
# print("Total arguments passed:", n)
# print("\nName of Python script:", sys.argv[0])
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
# 	print(sys.argv[i], end = " ")
# Sum = 0
# for i in range(1, n):
# 	Sum += int(sys.argv[i])
	
# print("\n\nResult:", Sum)




# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)



import sys
import time
def progress_bar(total):
    sys.stdout.write("[")
    for i in range(total):
        sys.stdout.write("#")  
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("]")
print(progress_bar(10)) 



# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
    


# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])





##API----------------------------------------------------------------------------------------------------------

##API - Application Programming Interface
##API is a set of rules and protocols that allows one software application to communicate with another software application.
##API is a way to access the functionality of a web server.
##JSON - JavaScript Object Notation
##JSON is a lightweight data-interchange format.



# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())



# import json
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))



# import json
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])



# import inflect
# def main():
#     p = inflect.engine()
#     names = []
#     try:
#         while True:
#             name = input()
#             names.append(name)
#     except EOFError:
#         pass

#     if names:
#         names_str = p.join(names)
#         print(f"Adieu, adieu, to {names_str}")

# main()



# import requests
# def main():
#     print("Search the Art Institute of Chicago collection")
#     artist = input("Artist: ")
#     try:
#         response = requests.get(
#             "https://api.artic.edu/api/v1/artworks/search",
#             {"q": artist})
#         response.raise_for_status()
#     except requests.HTTPError:
#         print("Error: could not retrieve search results")
#         return
    
#     content = response.json()
#     for artwork in content["data"]:
#         print(f"* {artwork["title"]}")
        
# main()




# import json
# numbers = [2, 3, 5, 7, 11, 13]
# with open("main/numbers.json", "w") as file:
#     json.dump(numbers, file)

# import json
# with open("main/numbers.json") as file:
#     numbers = json.load(file)
# print(numbers)


# import json
# try:
#     with open("main/name.json") as file:
#         name = json.load(file)
# except FileNotFoundError:
#     name = input("What is your name? ")
#     with open("main/name.json", "w") as file:
#         json.dump(name, file)
#         print(f"We will remember you when you come back, {name}")
# else:
#     print(f"Welcome back, {name}")





## Unit Testing----------------------------------------------------------------------------------


# def get_main(first, last, middle=""):
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()



# def location(city, country, population=""):
#     location = f"{city}, {country}"
#     if population:
#         full_loc = f"{location.title()} - population {population}"
#     else:
#         full_loc = location.title()
#     return full_loc




# class AnonymousSurvey:
#     def __init__(self, question):
#         self.question = question
#         self.responses = []

#     def show_question(self):
#         print(self.question)

#     def store_response(self, new_response):
#         self.responses.append(new_response)

#     def show_results(self):
#         print("Survey results:")
#         for response in self.responses:
#             print(f"- {response}")




