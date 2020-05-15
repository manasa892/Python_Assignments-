# -*- coding: utf-8


 
#2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.

a = []
for i in range(2000,3500):
    if (i % 7) == 0 and (i % 5 == 0):
        a.append(str(i))
print(a)
  
      
#3.Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name. 

First_name = input("Enter the First Name")
Last_name = input("Enter the Last Name ")

print(First_name ,"",Last_name)
    
#4.Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r

Diameter = 12
radius = Diameter/2
exponential = pow(radius,3)

volume = (4/3) * 3.141592 * exponential 
print (volume)
 

#Task 02 - Pgm no01 - Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.
 


req_val = input("Enter the Number : ")
list_of_val =[]
req_list=[]

list_of_val = req_val.split(",")
for i in list_of_val:
    req_list.append(int(i))
print (req_list)



#Task 02 - Pgm no 02 Create the Half Diamond pattern using nested for loop in Python. 
    
rows = int(input("Enter the number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(1, i - 1):
        print("*", end=' ')
    print(" ")
    
# Task 02 - Pgm no 03 - write a Python program to reverse a word after accepting the input from the user.

word = input("Enter the word to be reversed:")
word [::-1]

#Task 02 - Pgm no 04 - Write a Python Program to print the given string in the format specified in the sample output.
print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVERIGN,! \n\t\tSOCIALIST, SECULAR,DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")

