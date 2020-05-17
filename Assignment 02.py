# -*- coding: utf-8 -*-

#Assignment no 02 

#Task no 1 - pgm no 01 : Write a Python Program to implement your own myreduce() function which works exactly like
#Python's built-in function reduce()

def myreduce(anyfunc, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = anyfunc(result, item)
    return result 

def sum(x,y): return x + y

print ("Sum of the list [1,2,3,5] "   + str(myreduce(sum, [1,2,3,5])) )

# Task no 01 - pgm n0 02 - Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()

def myfilter(anyfunc, sequence):
    result = []
    for item in sequence:
       if anyfunc(item):
        result.append(item)
    return result


def ispositive(x):
 if (x >= 0): 
  return False 
 else: 
  return True

print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))
    
#Task 02 - Pgm no 03 - Implement List comprehensions to produce the following lists
#Write List comprehensions to produce the following Lists

# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

from functools import reduce

word = "ACADGILD"
alphabet_list = [alphabet for alphabet in word ]
print(alphabet_list)
 

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
given_list = ['x','y','z']
result = [item * num for item in given_list for num in range(1,5) ]
print (result)


# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
given_list = ['x','y','z']
result = [item * num for num in range(1,5) for item in given_list]
print (result)


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
given_list = [2,3,4] 
result = [[item+num] for item in given_list for num in range(0,3)]
print (result)   
    
# [[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]]
given_list = [2,3,4,5]
result = [[item + num for item in given_list] for num in range(0,4)]
print (result)

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
given_list = [1,2,3]
result = [(b,a) for a in given_list for b in given_list]
print (result)
    

#Task 03 - Pgm 03 - Implement a function longestWord() that takes a list of words and returns the longest one.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["first_word", "second_word",...]))
        

#Task 02 - pgm 1.1 - Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula. 
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Parent Class
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input("Enter side" +str(i+1)+" : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1,"is",self.sides[i])
            
#Sub Class
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
        
    def findArea(self):
        a, b, c = self.sides 
        #calculate the semi-perimeter
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %0.2f" %area)
        
#creating the object 
t = Triangle()  

#Invoking the functions 
t.inputSides()
t.dispSides()
t.findArea()


#Task 02 - pgm 1.2 - Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

#Creating the object 
longest_word = find_longest_word(["bindhu","kavya"])

#printing the longest_word
print(longest_word)


#Task 02 - pgm 2.1 - Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words.

wordlist = ["first_word","second_word",...]

def wordlength(wordlist):
    return list(map(lambda x: len(x),wordlist))

print ("word lengths in array => " +str(wordlength(wordlist)))
          
#Task 02 - pgm 2.2 - Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
#a vowel, False otherwise.

def vowel_check(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True 
    else:
        return False
    
char = input("Enter character : ")

if(char.isalpha() == False):
     exit();

#Invoking the function 
if (vowel_check(char)):
    print(char,"is a vowel");
else:
    print(char, "is not a vowel");



    
       