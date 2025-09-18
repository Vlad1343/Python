# "Practical Tasks"
"""Variables and Data Types"""

# # 1. 
# name = "Vlad"
# age = 13
# like = True
# print(f"{name}, {age}, {like}")


# # 2. Swap the values of two variables a and b without using a temporary variable.
# a = 3
# b = 5
# a, b = b, a


# 3. Ask the user for their birth year and calculate their current age (assume the current year is 2025).
# year = int(input("What's your birth year? "))
# age = 2025 - year
# print(f"You are {age} years old")


# 4. Convert the string "123.45" into a float and into an int (show both results)
# string = "123.45"
# float1 = float(string)
# int1 = int(float(string))
# print(float1)
# print(int1)


# 5. Given the variable x = "42", convert it into an int and add 8.
# x = "42"
# x_int = int(x)
# print(x_int+8)


# 6. Write a function guess_type(value: str) that:
	# •	takes a string input,
	# •	and tries to guess whether it represents an int, float, bool, or plain string.
	# •	Example:
	# •	"123" → int
	# •	"3.14" → float
	# •	"True" → bool
	# •	"hello" → string

# def guess_type(value):
#     # Check for boolean
#     if value.lower() in ("true", "false"):
#         return "bool"
#     # Check for int
#     try:
#         int(value)
#         return "int"
#     except ValueError:
#         pass
#     # Check for float
#     try:
#         float(value)
#         return "float"
#     except ValueError:
#         pass
#     # If nothing else, it's a string
#     return "string"

# # Test it
# user_input = input("Type any value: ")
# print(guess_type(user_input))



# 7.	Variable type tracker
# 	•	Create a list of 5 variables of different types.
# 	•	Write a loop that prints:
# Variable: <value>, Type: <type>, Is numeric? <True/False>

# list = ["hello", 5, 10.5, True, [1,2,3]]
# for i in list:
#     print(f"Variable: {i}, Type: {type(i)}, Is numeric? {isinstance(i, (int,float))}")




"""Operators & Expressions"""

# # 1.	Calculate the area of a rectangle with width = 5 and height = 7.
# print(5*7)
 

# # 2.	Calculate the perimeter of the same rectangle.
# print(2*(5+7))


# # 3.	Ask the user for a number and print whether it is even or odd.
# num = int(input("Num: "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")


# # 4.	Ask the user for two numbers and print:
# # •	Sum
# # •	Difference
# # •	Product
# # •	Division
# # •	Modulus

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)


# # 5. Without using **, write a function to compute x^y using a loop.

# def power(x, y):
#     result = 1
#     for _ in range(y):  # repeat y times
#         result *= x
#     return result

# # Example:
# print(power(2, 5))
# print(power(3, 4))

# #6. Ask for a number and check if it’s divisible by 2, 3, and 5, printing all divisors.
# num = int(input("Num: "))
# if num%2==0:
#     print("Divisible by 2")
# if num%3==0:
#     print("Divisible by 3")
# if num%5==0:
#     print("Divisible by 5")


# # 7. Ask for three numbers and print the largest using only arithmetic and comparison operators (no max()).
# a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
# if a > b and a > c:
#     print(f"{a} is the biggest")
# elif b > a and b > c:
#     print(f"{b} is the biggest")
# else:
#     print(f"{c} is the biggest")


# #8. Swap the digits of a two-digit number entered by the user.
# # 	•	Example: number = 34 → output: 43.
# num = input("Enter a two-digit number: ")
# swapped = num[::-1]
# print(swapped)


##! 9. Reverse a number (any length, not just 2 digits).
# 	# •	Example: 12345 → 54321.
# 	# •	Don’t just use slicing like [::-1] — try solving it with a loop and arithmetic.
 
# num = input("Enter a number: ")
# digits = list(num)
# reversed = []

# # loop backwards over the original list
# for i in range(len(digits)-1, -1, -1):
#     reversed.append(digits[i])

# # join the list back into a string
# reversed_num = "".join(reversed)
# print(reversed_num)



##! 10. Check if a number is a palindrome.
# # 	•	A palindrome reads the same forward and backward.
# # 	•	Example: 121 → palindrome, 123 → not palindrome.
# num = input("Enter a number: ")
# num_list = list(num)
# is_palindrome = True

# for i in range(len(num_list)//2):
#     if num_list[i] != num_list[-(i+1)]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("It's a palindrome")
# else:


# !11. Find the greatest common divisor (GCD) of two numbers (without using math.gcd).
# # 	•	Example: (36, 60) → 12.
# # 	•	Try using the Euclidean algorithm (harder version).
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# while num2>0:
#     remainder = num1%num2
#     num1, num2 = num2, remainder
# print(f"GCD: {num1}")


# # 12. Count the number of digits in a number
# # 	•	Example: 12345 → 5 digits
# # 	•	Solve once with strings, then try pure arithmetic (optional)
# num = input("Enter number: ")
# num_of_digits = len(num)


# # !13. Check Armstrong number
# # 	•	A number is Armstrong if the sum of its digits raised to the power of the number of digits equals the number.
# # 	•	Examples: 153 → 1³+5³+3³ = 153 ✅, 9474 → 9⁴+4⁴+7⁴+4⁴ = 9474 ✅
# num = int(input("Enter number: "))
# digits = [int(d) for d in str(num)]
# num_digits = len(digits)

# armstrong_sum = 0
# for d in digits:
#     armstrong_sum += d ** num_digits  # raise each digit to total number of digits

# if armstrong_sum == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is NOT an Armstrong number")



#! # 14. Find all prime numbers up to n
# # 	•	Input: 20 → Output: [2, 3, 5, 7, 11, 13, 17, 19]
# # 	•	First with basic loops, then (harder) optimize to avoid unnecessary checks.
# n = int(input("Find primes up to: "))
# primes = []

# for num in range(2, n + 1):  # start from 2
#     is_prime = True
#     for i in range(2, num):  # check divisibility
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)

# print(primes)




# Other
# num = 413
# digits = [int(d) for d in str(num)]
# print(digits)   # [4, 1, 3]



##! 9. Reverse a number (any length, not just 2 digits).
# 	# •	Example: 12345 → 54321.
# 	# •	Don’t just use slicing like [::-1] — try solving it with a loop and arithmetic.
num = list(int(input("Num: ")))
reversed = []
for i in range(len(num)-1,-1,-1):
    reversed.append(num[i])
