
def binary_search(list, item):
    low = 0 
    high = len(list)-1
    
    while low <= high: 
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else: 
            low = mid + 1
    return None 

my_list = [1, 3, 5, 7, 9] 
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None











## Recursive binary search.

# def binary_search(arr, low, high, x):

#     if high >= low:
#         mid = (high + low) // 2

#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid

#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)

#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)

#     else:
#         # Element is not present in the array
#         return -1

# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")





## Iterative Binary Search Function
## It returns index of x in given array arr if present,
## else returns -1
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0

#     while low <= high:
#         mid = (high + low) // 2

#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1

#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1

#         # means x is present at mid
#         else:
#             return mid

#     # If we reach here, then the element was not present
#     return -1

# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
# result = binary_search(arr, x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")



# import bisect
# def binary_search_bisect(arr, x):
#     i = bisect.bisect_left(arr, x)
#     if i != len(arr) and arr[i] == x:
#         return i
#     else:
#         return -1
 
# arr = [2, 3, 4, 10, 40]
# x = 10
# result = binary_search_bisect(arr, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")