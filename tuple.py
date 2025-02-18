

# user_data = ("joe_17",)
# print(user_data)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# def get_scores(scores_list):
#   high = max(scores_list)
#   low = min(scores_list)
#   return high, low
# scores = [31, 17, 62]
# data = get_scores(scores)
# print(data)
  
# def top_3(players):
#   return players[0], players[1], players[2]
# players = ["Tom", "Martin", "Jake", "Andrew"]
# top_three = top_3(players)
# print(f"First: {top_three[0]}")
# print(f"Second: {top_three[1]}")
# print(f"Third: {top_three[2]}")

# scores = [("mia", 75), ("lee", 90)]
# print(scores)

# grocery_list = ["broccoli", "potato", "broccoli", "milk"]
# print(set(grocery_list))

# friends = {"Emma", "Jen", "Rob", "Ed"}
# chat = {"Jen", "Ed"}
# print(chat.issubset(friends))

# classmates = {"Sue", "Paul"}
# friends = {"Don", "Sue"}
# print(classmates.union(friends))          #all elements
# print(classmates.intersection(friends))   #common
# print(classmates.difference(friends))     #present in {classmates}, but not in {frieds}

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates     #unpacking