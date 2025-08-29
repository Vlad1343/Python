


# FILE I/O----------------------------------------------------------------------------------------------------------

# File I/O is the ability of a program to take a file as input or create a file as output.



# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()



# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
    
    
    
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print("hello,", line.rstrip())
    
    

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())




# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")
    
    


# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip)






# CSV Files----------------------------------------------------------------------------------------------------------

# CSV stands for Comma Separated Values. It is a simple file format used to store
# tabular data, such as a spreadsheet or database.



# with open("file/names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")



# with open("file/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
        
        
        
# students = []
# with open("file/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)



# students = []
# with open("file/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")
    
    


# students = []
# with open("file/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append({"name": name, "house": house})

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")
# print()

# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")




# students = []
# with open("file/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append({"name": name, "house": house})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")




# import csv
# students = []
# with open("file/students1.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})
        
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
    
    
    

# import csv
# students = []
# with open("file/students1.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#         # students.append(row)
        

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")



# import csv
# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("file/students2.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow({name, home})
    

    
    
# import csv
# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("file/students2.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})



# import csv
# with open("file/students1.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
#         for row in reader:
#                 print(row[0])
#                 print(f"{row[0]} is from {row[1]}")
            


# import csv
# with open("file/students1.csv", "r") as file:
#         reader = csv.reader(file)
#         with open("file/new_names.csv", "w") as file2:
#             writer = csv.writer(file2, delimiter="-")
#             for row in reader:
#                 writer.writerow(row)
                
                

# import csv
# with open("file/students1.csv", "r") as file:
#         reader = csv.DictReader(file)
#         for line in reader:
                # print(line)
                # print(f"{line['name']} is from {line['home']}")
                # print(line["name"])



# filename = "pi_million_digits.txt"
# with open(filename) as file:
#     lines = file.readlines()
# pi_string = ""
# for line in lines:
#         pi_string += line.rstrip()
# birthdays = input("Enter your birthday, in the form mmddyy: ")
# if birthdays in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# file = open("test.txt", "w")
# file.write("Hello, World!\nI'm Vlad")
# file.close()
#or
# with open("test.txt", "w") as file:
#   file.write("Hello, World!\nI'm Vlad")


# with open("test.txt", "r") as file:
#   text = file.read()
#   print(text)
  
  
# with open("test.txt", "a") as file:
#   file.write("\nNew addition")


# with open("file/learning_python.txt") as file:
#         contents = file.read()
# print(contents)
        
        
        
# with open("file/learning_python.txt") as file:
#         for line in file:
#                 print(line.replace("Python", "C").rstrip())
        
        
        
# with open("file/learning_python.txt") as file:
#         lines = file.readlines()
# for line in lines:
#         print(line.rstrip())



# with open("file/learning_python.txt", "a") as file:
#         file.write("\nI love programming in Python!")



# with open("file/learning_python.txt", "r") as file:
#     contents = file.read().lower()
#     count = contents.count("you")
#     print(count)
        


# while True:
#         try:
#                 number = int(input("Enter a number: "))
#         except ValueError:
#                 print("That's not a number!")
#                 pass










# Binary Files and PIL----------------------------------------------------------------------------------------------------------

# Binary files are files that contain data that is not human-readable. 
# Examples include images, videos, and executables.


# import sys
# from PIL import Image
# images = []

# for arg in sys.argv[1:]:
#     image = Image.open(arg)
#     images.append(image)

# images[0].save(
#     "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=10
# )
# # python file/file_io.py costume1.gif costume2.gif




# from PIL import Image
# from PIL import ImageFilter
# def main():
#     with Image.open("python1.jpg") as image:
#         print(image.size)
#         print(image.format)
        # image.rotate(180).save("rotated.gif")
        # image.filter(ImageFilter.BLUR).save("blurred.gif")
        # image.filter(ImageFilter.CONTOUR).save("contour.gif")
        # image.filter(ImageFilter.FIND_EDGES).save("contour1.gif")
        

# main()





# import csv
# import numpy as np
# from PIL import Image
# def main():
#     with open("file/students2.csv", "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(f"{row['name']} is from {row['home']}")

# brightness = 0
# def calculate_brightness(filename):
#     with Image.open(filename) as image:
#         brightness == np.mean(np.array(image.convert("L"))) / 255
#     return brightness

# main()





# def main():
#     with open("file/students2.csv", "r") as file:
#         contents = file.readlines()
    
#     chapter1 = contents[0:10]
#     with open("file/chapter1.txt", "w") as file:
#         file.writelines(chapter1)

# main()