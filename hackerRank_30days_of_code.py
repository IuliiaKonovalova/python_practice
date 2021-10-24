# Day 1

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
# j = int(input())
# e = float(input())
# t = input()
j = 5
e = 3.0
t = 'here'

# Print the sum of both integer variables on a new line.
print(i+j)
# Print the sum of the double variables on a new line.
print(d+e)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+t)

#  Day 2


def solveMeal(meal_cost, tip_percent, tax_percent):
    # Write your code here
    
    total = meal_cost + meal_cost/100*tip_percent + meal_cost/100*tax_percent
    return round(total)


print(solveMeal(100, 15, 8))

# Day 3

N = 5
print('Weird' if N % 2 != 0 or 6 <= N <= 20 else "Not Weird")

# Day 4

class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        self.age = 0
        if initialAge < 0:
          print('Age is not valid, setting age to 0.')
        else:
          self.age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
          print("You are a teenager.")
        elif self.age >= 18:
          print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):

        global age
        self.age += 1
        # Increment the age of the person in here

# Day 5

    # n = int(input().strip())
    n = 5
    result = 0
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')


# Day 6


# for i in range(int(input())):
#     s=input()
#     print(*["".join(s[::2]),"".join(s[1::2])])

words_for_split = [5, 'Hacker', 'Rank']

for i in range(words_for_split[0]):
    print(*["".join(words_for_split[::2]),"".join(words_for_split[1::2])])

words_for_split = [2, 'Hacker', 'Rank']
words_for_split2 = ['Hacker', 'Rank']
break_in_word = int(words_for_split.pop(0))
first_word = words_for_split.pop(0)
second_word = words_for_split.pop()
print(break_in_word)
print(*["".join(first_word[::2]),"".join(first_word[1::2])])
print(*["".join(second_word[::2]),"".join(second_word[1::2])])


for i in words_for_split2:
  # words_for_split2 = ['Hacker', 'Rank']
  print(*["".join(i[::2]),"".join(i[1::2])])


#  Day 7

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print(' '.join(map(str, arr[::-1])))
    

        
#  Day 8

number_of_contacts = int(input())
dic = {}
for _ in range(number_of_contacts):
    name, number = input().split()
    dic[name] = number

while True: 
    try:
        name = input()
        if name in dic.keys():
            
            print(name + "=" + dic[name])
        else:
            print("Not found")
    except EOFError:
        break


# Day 9

def factorial(n):
    
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# Day 10

if __name__ == '__main__':
    n = int(input().strip())
current_consecutive_ls = 0

max_consecutive_ls = 0

while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_ls += 1
        if current_consecutive_ls > max_consecutive_ls:
            max_consecutive_ls = current_consecutive_ls
    else:
        current_consecutive_ls = 0
    n = n // 2
print(max_consecutive_ls)

# Day 11

grid = list()

for i in range(6):
    row = input().strip().split(' ')
    row = list(map(int, row))
    grid.append(row)

def _get_hourglass_sum(grid, i, j):
    sum = 0
    sum += grid[i-1][j-1]
    sum += grid[i-1][j]
    sum += grid[i-1][j+1]
    sum += grid[i][j]
    sum += grid[i+1][j-1]
    sum += grid[i+1][j]
    sum += grid[i+1][j+1]
    return sum

# start max_hourglass_sum at smallest possible hourglass
max_hourglass_sum = -63
for i in range(1,5):
    for j in range(1, 5):
        current_hourglass_sum = _get_hourglass_sum(grid, i, j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum

print(max_hourglass_sum)


# Day 12

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores
        
    # Write your function here
    
    def calculate(self):
        sum_of_scores = 0
        for score in scores:
            sum_of_scores += score
        average_scores = sum_of_scores / len(scores)
        if average_scores < 40:
            return 'T'
        elif average_scores < 50:
            return 'D'
        elif average_scores < 70:
            return 'P'
        elif average_scores < 80:
            return 'A'
        elif average_scores < 90:
            return 'E'
        else:
            return 'O'

            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())



# Day 13

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')
 
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

# Day 14

# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#         self.maximumDifference = 0
#     def computeDifference(self):
#         set_of_elements = sorted(self.__elements)
#         min_element = 101
#         max_element = 0
#         for element in set_of_elements:
#             if element < min_element:
#                 min_element = element
#             elif element > max_element:
#                 max_element = element
#             else:
#                 pass
#         self.maximumDifference = max_element - min_element
# 	# Add your code here

# # End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]

# d = Difference(a)
# d.computeDifference()

# print(d.maximumDifference)

# Day 15


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        if head is None:
            self.head = new_node
            return self.head
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return self.head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)    
mylist.display(head); 

# Day 16 

S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
        
        
# Day 17




class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n, p)
    


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   