
# from random import randint
# from random import choice
# players = ['vlad', 'max', 'john', 'marta'] 
# a = randint(1,6)
# print(a)
# players = choice(players)
# print(players)

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


# names = ["John", "Bob", "Sara", "Mary", "Mike"]
# print(names[-1])
# print(names[2:])
# names[0] = "Vlad"
# print(names)

# list = [0, 12, 73, -32, 77, 196]
# max = list[0]
# for i in list:
#   if i > max:
#     max = i
# print(max)
# print(max(list))

# numbers = [5, 2, 7, 12, 1]
# print(numbers.index(5))
# print(50 in numbers)
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(5)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.clear()
# print(numbers)

# numbers = [5, 2, 7, 12, 1, 5]
# print(numbers.count(5))
# print(numbers.sort())
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [5, 2, 7, 12, 1, 5]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)

# numbers = [5, 2, 7, 12, 1, 2, 5, 7]
# uniques = []
# for i in numbers:
#   if i not in uniques:
#     uniques.append(i)
# print(uniques)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#   output = ""
#   for count in range(x_count):
#     output += "x"
#   print(output)

# prices = [10, 38, 40, 58, 62]
# halved = []
# for price in prices:
#   half_price = int(price/2)
#   halved.append(half_price)
# print(halved)

# prices = [10, 38, 40, 58, 62]
# halved = [price/2 for price in prices]
# print(halved)

# winners = ["John", "Helen", "Sigmund", "Olaf"]
# del winners[-1]
# print(winners)

# scores = [100, 200, 300, 400, 500]
# print(scores[0:2:-1])                      #start:stop:step
# print(scores[4:1:-1])

# rng = range(10)
# print(list(rng))



# def longer_than_4(self):
#     return len(self) > 4

# strings = ["John", "Helen", "Sigmund", "Olaf"]
# filtered = filter(longer_than_4, strings) 
# filtered = filter(lambda x: len(x)>4, strings)
# lengths = map(len, strings)
# print(list(lengths))

# lengths = map(lambda x: x + "s", strings)
# print(list(lengths))

# print(list(filtered))


# numbers = [1, 2, 3, 4, 5, -7, -4]
# print(sorted(numbers))
# a = sorted(numbers, reverse = True)
# print(a)



# names = ["Alice", "Bob", "Charlie", "David", "Tim"]
# ages = [30, 25, 35, 20]

# for idx in range(min(len(names), len(ages) ) ) :
#     name = names [idx]
#     age = ages [idx]
#     print (f"{name} is {age} years old")
#or
# combined = list(zip(names,ages))
# for name, age in combined:
#     print(f"{name} is {age} years old")




# SHOWS = [
#     "Avatar: The last airbender",
#     "Ben 10",
#     "Arthur",
#     "Spongebob Squarepants",
#     "Phineas and ferb",
#     "Kim possible",
#     "Jimmy Neutron",
#     "the Proud family "
# ]

# def main():
#     cleaned_shows = []
#     for show in SHOWS:
#         cleaned_shows.append(show.strip().title())
    
#     print(', '.join(cleaned_shows))

# main()




# students = ["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i + 1, students[i], sep=". ")



# results = ["Mario", "Luigi"]
# results.extend(["Bowser", "Yoshi"])
# results.remove("Mario")
# results.insert(0, "Toad")
# print(results)
# results.reverse()
# print(results)



# def main():
#     history = []
    
#     while True:
#         action = input("Action: ").lower()
#         if action == "undo":
#             undone = history.pop()
#             print(f"Undone: {undone}")
#         elif action == "restart":
#             history.clear()
#         else:
#             history.append(action)
#         print(history)

# main()




# names = ["Alice", "Bob", "Charlie", "David", "Tim"]
# names_copy = names.copy()
# names_copy.remove("Tim")
# print(names)
# print(*names)
# print(names_copy)



# nums = [3,1,2,10,1]
# class Solution(object):
#     def runningSum(self, nums):
#         for i in range(1,len(nums)):
#             nums[i]+=nums[i-1]
#         return nums

# s = Solution()
# print(s.runningSum(nums))





















## LIST COMPREHENSION ===========================================================================================




# people = ["Alice", "Bob", "Charlie", "David", "Tim"]

# long_names = []
# for person in people:
#     if len(person) > 4:
#         long_names.append(person)
#or
# long_names = [person for person in people if len(person) > 4]
# print(f"Long names: {long_names}")








# # 2D LISTS  -----------------------------------------------------------------------------------------------------------------------

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# matrix [0][1] = 20
# print(matrix[0][1])
# for row in matrix:
#   for item in row:
#     print(item)
