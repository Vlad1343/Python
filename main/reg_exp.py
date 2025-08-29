

## Regular Expressions -------------------------------------------------------------------------------------------------------

## Regular expressions or “regexes” will enable us to examine patterns within our code


# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")


# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")



## import re    ##Regular expressions
## .   any character except a new line
## *   0 or more repetitions
## +   1 or more repetitions
## ?   0 or 1 repetition
## {m} m repetitions
## {m,n} m-n repetitions
## ^   matches the start of the string
## $   matches the end of the string or just before the newline at the end of the string
## []    set of characters
## [^]   complementing the set    

##! Raw strings - strings that don’t format special characters—
## instead, each character is taken at face-value

##\d    decimal digit
##\D    not a decimal digit
##\s    whitespace characters
##\S    not a whitespace character
##\w    word character, as well as numbers and the underscore
##\W    not a word character

##A|B     either A or B
##(...)   a group
##(?:...) non-capturing version

##re.IGNORECASE
##re.MULTILINE
##re.DOTALL


# import re
# email = input("What's your email? ").strip()
# if re.search(r"^\w+@\w+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")


# import re
# email = input("What's your email? ").strip()
# if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")


# import re
# email = input("What's your email? ").strip()
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")


# import re
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")


# import re
# name = input("What's your name? ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):      # := - walrus operator
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")







## Extracting User Input ------------------------------------------------------------------------------------------------


# url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")


# url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")


# import re
# url = input("URL: ").strip()
# username = re.sub(r"https://twitter.com/", "", url)
# print(f"Username: {username}")


# import re
# url = input("URL: ").strip()
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
#     print(f"Username:", matches.group(1))