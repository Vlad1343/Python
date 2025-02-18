#Shift+tab 

# a = int(input('Введіть годину дня: '))
# if a>=6 and a<=12:
#    print('Ранок')
# elif a>=13 and a<=18:
#   print('День')
# elif a>=19 and a<=23:
#   print('Вечір')
# elif a==24:
#   print('Ніч')
# elif a>=1 and a<=5:
#   print('Ніч')
# else:
#   print('Помилка')


# number1 = 20
# number2 = 30
# if number1 * number2 <= 1000:
#   print(number1*number2)
# else:
#   print(number1+number2)


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper( ) == "L":
  converted = weight * 0.45
  print(f"You are {converted} kilos")
else:
  converted = weight / 0.45
  print(f"You are {converted} pounds")

networks = ["open-WIFI", "guest", "Wi-Fly"]
open_networks = [wifi for wifi in networks if wifi.count("open") > 0]
print(open_networks)