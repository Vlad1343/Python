
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# tropical = ['toy', 'car']
# thisset.update(tropical)
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)


# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)


# answers = {"yes", "no"}
# answers.add("maybe")
# print(answers)



# students = [
#     {"name": "John", "age": 20},
#     {"name": "Jane", "age": 23},
#     {"name": "Jim", "age": 20},
#     {"name": "Jack", "age": 23},
#     {"name": "Jill", "age": 24}
# ]
# list = []
# for i in students:
#     if i["age"] not in list:
#         list.append(i["age"])
# for age in sorted(list):
#     print(age)


students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 23},
    {"name": "Jim", "age": 20},
    {"name": "Jack", "age": 23},
    {"name": "Jill", "age": 24}
]
list = set()
for i in students:
    list.add(i["age"])
for age in sorted(list):
    print(age)