
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
#   ":(": "😕"
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
