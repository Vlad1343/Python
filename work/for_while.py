
# for i in range(1,6):
#   if i == 2:
#     continue
#   print(i)

# for i in range(1,6):
#   if i == 3:
#     break
#   print(i)

# prev_num = 0
# for i in range(1,11):
#   sum = prev_num + 1
#   print(i, prev_num, sum)
#   prev_num = i


# a = input("Enter any string: ")
# b = len(a)
# for i in range(0, b-1, 2):
#   print('index[", i, "]', a[i])
  
# a = input("Enter any string: ")
# b = list(a)
# for i in b[0::2]:
#   print(i)

# for item in ['Jack', 'Sara', 'Vlad']:
#   print(item)
  
# for item in range(5,10,2):
#   print(item)

# prices = [10, 20, 30]
# total = 0
# for i in prices:
#   total += i
# print(f"Total: {total}")
  

## WHILE  -----------------------------------------------------------------------------------------------------------------------


# i = 1
# while i <= 5:
#   print(i)
#   i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#   guess = int(input('Guess: '))
#   guess_count += 1
#   if guess == secret_number:
#     print("You won")
#     break
# else:
#   print("You failed")
    
    
# command = ""
# started = False
# print("Type \033[1mhelp\033[0m for info")
# while True:
#   command = input("> ").lower()
#   if command == "start":
#     if started:
#       print("Car has already started")
#     else:
#       started = True
#       print("Car started...")
#   elif command == "stop":
#     if not started:
#       print("Car has already stopped")
#     else:
#       started = False
#       print("Car stopped")
#   elif command == "help":
#     print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#           """)
#   elif command == "quit":
#     print("You have quitted the game!")
#     break
#   else:
#     print("Error. Try again")
  
  
## NESTED LOOP  -----------------------------------------------------------------------------------------------------------------------

# for x in range(4):
#   for y in range(3):         #inner loop
#     print(f"({x}, {y})")


# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#   output = ""
#   for count in range(x_count):
#     output += "x"
#   print(output)
