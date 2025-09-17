
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict["brand"])
# x = thisdict.get("fuel")
# print(x)
# print(thisdict.get("fuel", "No data"))
# thisdict["colour"] = "Red"
# print(thisdict["colour"])

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x)
# car["color"] = "white"
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x)
# car["year"] = 2020
# print(x)

# x = {'type' : 'fruit', 'name' : 'banana'}
# print(x)
# x.update({'name': 'apple'})
# print(x)

# dictionary_tk = {
#   "name": "Leandro",
#   "nickname": "Tk",
#   "nationality": "Brazilian"
# }
# print("My name is %s" %(dictionary_tk["name"]))
# print("But you can call me %s" %(dictionary_tk["nickname"]))
# print("And by the way I'm %s" %(dictionary_tk["nationality"]))

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


# actor_bio = {
#   "name": "Bill Muray",
#   "known for": ["Lost in Translation", "Rushmore"]
# }
# print(actor_bio["known for"][0])
# for i in actor_bio:
#   print(actor_bio[i])


# toppings = {
#   "olives": True,
#   "anchovies": False,
#   "extra cheese": False
# }
# toppings["olives"] = False
# print(toppings)


# phone = input("Your phone number: ")
# digits = {
#   "1": "One",
#   "2": "Two",
#   "3": "Three",
#   "4": "Four"
# }
# output = ""
# for i in phone:
#   output += digits.get(i, "!") + " "
# print(output)


# message = input("> ")
# words = message.split(" ")
# emojis = {
#   ":)": "🙂",
#   ":(": "😕",
# }
# output = ""
# for word in words:
#   output += emojis.get(word, word) + " "
# print(output)


# product = {
#   "category": "book",
#   "price": 4.99,
#   "in_shop": True
# }
# del product["in_shop"]
# print(product)



# people = [
#     {"name": "John", "age": 18},
#     {"name": "Marta", "age": 21},
#     {"name": "Oliver", "age": 23},
#     {"name": "John", "age": 44},
# ]
# sorted_people = sorted(people, key=lambda person: person["age"])
# print(sorted_people)




# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for i in students:
#     print(i, students[i], sep=", ")



# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")




# def main():
#     spacecraft = {"name": "Voyager 1", "distance": 163}
#     spacecraft.update({"orbit": "Sun"})
#     spacecraft1 = {"name": "SpaceX 32"}
#     print(create_report(spacecraft, spacecraft1))
# def create_report(spacecraft, spacecraft1):
#     return f"""
# ======== REPORT ========

# Name: {spacecraft["name"]}
# Distance: {spacecraft["distance"]} AU
# Orbit: {spacecraft.get("orbit", "Unknown")}

# Name: {spacecraft1["name"]}
# Distance: {spacecraft1.get("distance", "Unknown")} AU
# Orbit: {spacecraft1.get("orbit", "Unknown")}

# ========================
# """

# main()
    
    
    
    
    
    
    
# def main():
#     combined = {
#         "spacecraft1": {"name": "Voyager 1", "distance": 163, "orbit": "Sun"},
#         "spacecraft2": {"name": "SpaceX 32"}
#     }
#     print(create_report(combined))

# def create_report(combined):
#     sc1 = combined["spacecraft1"]
#     sc2 = combined["spacecraft2"]
#     return f"""
# ======== REPORT ========


# Name: {sc1["name"]}
# Distance: {sc1["distance"]} AU
# Orbit: {sc1.get("orbit", "Unknown")}


# Name: {sc2["name"]}
# Distance: {sc2.get("distance", "Unknown")} AU
# Orbit: {sc2.get("orbit", "Unknown")}


# ========================
# """





# distances = {
#     "Voyager 1": 163,              #key: value
#     "Voyager 2": 136,   
#     "Pioneer 10": 80,
#     "New Horizons": 58,
#     "Pioneer 11": 44
# }

        
# def main():
#     for distance in distances.values():
#         print(f"{distance} AU is {convert(distance)} m ")
#     print("")
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from Earth")


# def convert(au):
#     return au * 149597870700

# main()




# words = {"pair": 4, "hair": 4, "chair": 5, "graphic": 7}

# def main():
#     total = 0
#     print("Welcome to Spelling Bee!")
#     print("Your letters are: A I P C R H G")
#     while len(words) > 0:
#         count = len(words)
#         if count == 1:
#             print("1 word left!")
#         else:
#             print(f"{count} words left!")
#         print(f"Total points: {total}")
#         guess = input ("Guess a word: ")
#         if guess == "graphic":
#             words.clear()
#             print("You have won")
#         if guess in words.keys():
#             points = words.pop(guess)
#             total += points
#             print(f"Good job! You scored {points} points")
        
#     print("That's the game!")
#     if guess != "graphic":
#         print(f"Score: {total}")
    
# main()

          
          


# words = {"pair": 4, "hair": 4, "chair": 5, "graphic": 7}

# def main():
#     print("Welcome to Spelling Bee!")
#     for word, points in words.items():
#         print(f"{word.capitalize()} was worth {points} points")


# main()

          
 
 
 
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# thisdict["color"] = "red"
# print(thisdict)

# for x in thisdict:
#   print(thisdict[x])
# for x in thisdict.values():
#   print(x)
  
# for x in thisdict.keys():
#   print(x)

# for x, y in thisdict.items():
#   print(x, y)




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# mydict = dict(thisdict)
# print(mydict)




# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# # print(myfamily["child2"]["name"])

# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])



# ages = {'Alice': 30, 'Bob': 25}
# print(ages.get('Alice', 0))   # Alice is present → prints 30
# print(ages.get('Carol', 0))   # Carol not present → prints 0 (the default)



# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# freq = {}
# for f in fruits:
#     freq[f] = freq.get(f, 0) + 1
# print(freq)



# book = dict()
# book["apple"] = 1.2
# book["banana"] = 0.8
# book["orange"] = 1.0
# book["kiwi"] = 1.5
# print(book)
# print(book["banana"])



# voted = {}
# def check_voter(name):
#     if voted.get(name):
#         print("kick them out!")
#     else:
#         voted[name] = True
#         print("let them vote!")
# check_voter("tom")
# check_voter("mike")
# check_voter("mike")




# Dictionary Comprehensions

# dict_comp = {}
# for value in collection:
#     if condition:
#         dict_comp[key-expr] = value-expr
        
# dict_comp = {key-expr: value-expr for value in collection if condition}