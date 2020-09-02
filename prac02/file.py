"""This program gets input from user and writes it in a file"""


user_name = input("Enter name: ")   # Gets input from user
name_file = open("name.txt", "w")   # Opens file and write
print("Your name is ", user_name, file=name_file)   # Prints string with user input to file

open_file = open("numbers.txt", "r")
num1 = int(open_file.readline())
num2 = int(open_file.readline())
open_file.close()
print(num1 + num2)