
## Selection Sort

# def findSmallest(arr): 
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr

# print(selectionSort([5, 3, 6, 2, 10]))




## The call stack --------------------------------------------------------------------------------------

## It is a data structure that stores information about the active subroutines of a computer program.

# def greet(name):
#     print("hello, " + name + "!")
#     greet2(name)
#     print("Getting ready to say bye...")
#     bye()

# def greet2(name):
#     print("how are you, " + name + "?")

# def bye():
#     print("ok bye!")
# greet("John")



def fact(x):
 if x == 1:
    return 1
 else:
    return x * fact(x-1)
print(fact(5))