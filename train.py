# "Practical Tasks"
"""Variables and Data Types"""


# Convert the string "123.45" into a float and into an int (show both results)
# string = "123.45"
# float1 = float(string)
# int1 = int(float(string))
# print(float1)
# print(int1)



# Write a function guess_type(value: str) that:
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



# 	Variable type tracker
# 	•	Create a list of 5 variables of different types.
# 	•	Write a loop that prints:
# Variable: <value>, Type: <type>, Is numeric? <True/False>

# list = ["hello", 5, 10.5, True, [1,2,3]]
# for i in list:
#     print(f"Variable: {i}, Type: {type(i)}, Is numeric? {isinstance(i, (int,float))}")




"""Operators & Expressions"""


# # Without using **, write a function to compute x^y using a loop.

# def power(x, y):
#     result = 1
#     for _ in range(y):  # repeat y times
#         result *= x
#     return result

# # Example:
# print(power(2, 5))
# print(power(3, 4))



# # Ask for three numbers and print the largest using only arithmetic and comparison operators (no max()).
# a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
# if a > b and a > c:
#     print(f"{a} is the biggest")
# elif b > a and b > c:
#     print(f"{b} is the biggest")
# else:
#     print(f"{c} is the biggest")


## Swap the digits of a two-digit number entered by the user.
# # 	•	Example: number = 34 → output: 43.
# num = input("Enter a two-digit number: ")
# swapped = num[::-1]
# print(swapped)


##! Reverse a number (any length, not just 2 digits).
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



##! Check if a number is a palindrome.
# # 	•	A palindrome reads the same forward and backward.
# # 	•	Example: 121 → palindrome, 123 → not palindrome.
# num = input("Enter a number: ")
# num_list = list(num)
# is_palindrome = True

# for i in range(len(num_list)//2):
#     if num_list[i] != num_list[-(i+1)]:
#         is_palindrome = False
#         break


##! Find the greatest common divisor (GCD) of two numbers (without using math.gcd).
# # 	•	Example: (36, 60) → 12.
# # 	•	Try using the Euclidean algorithm (harder version).
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# while num2>0:
#     remainder = num1%num2
#     num1, num2 = num2, remainder
# print(f"GCD: {num1}")


# #  Count the number of digits in a number
# # 	•	Example: 12345 → 5 digits
# # 	•	Solve once with strings, then try pure arithmetic (optional)
# num = input("Enter number: ")
# num_of_digits = len(num)


# #! Check Armstrong number
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



#!# Find all prime numbers up to n
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



"""Strings"""

## Create a string "Hello, World!" and print only:
# 	# •	the first 5 characters,
# 	# •	the last 6 characters,
# 	# •	the string in uppercase,
# 	# •	the string in lowercase.
# string = "Hello, World!"
# print(string[0:5])
# print(string[-6:])
# print(string.upper())
# print(string.lower())


# # Ask the user for their name and print:
# # •	"Hello, <name>!",
# # •	the length of their name,
# # •	the first and last letter of their name.

# name = input("Enter your name: ")
# print(len(name))
# print(name[0])
# print(name[-1])


# # Given the string "python", print it reversed in two ways:
# # •	using slicing,
# # •	using a loop.
# string = "python"
# print(string[::-1])

# string = "python"
# digits = list(string)
# reversed = []
# for i in range(len(string)-1,-1,-1):
#     reversed.append(digits[i])

# res = "".join(reversed)
# print(res)


# # Ask the user for a sentence and count how many vowels (a, e, i, o, u) are in it.
# sentence = input("Enter your sentence: ")
# count = 0
# vowels = ['a', 'e', 'i', 'o', 'u'].lower()
# for i in sentence:
#     if i in vowels:
#         count += 1
# print(count)


# Check if a string is a palindrome (again, but now using string operations instead of lists).
# word = input("Enter your word: ")
# if word == word[::-1]:
#     print("palindrome")


# word = input("Enter a word: ").lower().replace(" ", "")
# word_list = list(word)
# is_palindrome = True

# for i in range(len(word_list)//2):
#     if word_list[i] != word_list[-(i+1)]:
#         is_palindrome = False
#         break



# # Replace all spaces in a string with "-" and print the result.
# sentence = input("Enter your sentence: ")
# new = sentence.replace(" ", "-")
# print(new)

    
# sentence = input("Enter your sentence: ")
# new_sentence = ""
# for char in sentence:
#     if char == " ":
#         new_sentence += "-"
#     else:
#         new_sentence += char
# print(new_sentence)



# # !Ask the user for a sentence and print the most common character (ignoring spaces).
# sentence = input("Enter your sentence: ").lower().replace(" ", "")
# counts = {}  # dictionary to store character counts
# for char in sentence:
#     if char.isalpha():  # only letters
#         if char in counts:
#             counts[char] += 1
#         else:
#             counts[char] = 1

# # find the character with the maximum count
# most_common_char = max(counts, key=counts.get)
# print(f"The most common character is '{most_common_char}' with {counts[most_common_char]} occurrences.")
        




# Write a function is_anagram(s1, s2) that checks if two strings are anagrams (contain the same letters in a different order).
# 	•	Example: "listen" and "silent" → ✅.
# 	•	"python" and "typhon" → ✅.
# 	•	"apple" and "pale" → ❌.




# Encode a string with a simple Caesar cipher (shift each letter by 3).
# 	•	Example: "abc" → "def".
# 	•	Bonus: also write a decoder.