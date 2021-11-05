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


# Day 18: Queues and Stacks


import sys
from collections import deque
class Solution:

    def __init__(self):
        self.stack = list()
        self.queue = deque()
    
    def pushCharacter(self, character):
        self.stack.append(character)
    
    def enqueueCharacter(self, character):
        self.queue.append(character)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.popleft()
    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    


# Day 19: Interfaces


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        temp = []
        for i in range(1, n+1):
            if n%i == 0:
                temp.append(i)
        return sum(temp)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)


# Day 20: Sorting

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    total_number_of_swaps = 0
    for i in range(n):
        number_of_swaps = 0
        for j in range (n - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                number_of_swaps += 1
        total_number_of_swaps += number_of_swaps
        if number_of_swaps == 0:
            break
print(f'Array is sorted in {total_number_of_swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}')

# Day 21 (Java 8)

    # public void printArray(T[] elements) {
    #     for (T element : elements) {
    #         System.out.println(element);
    #     }
    # }

    # Day 22
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       

# day 23

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        nodes_to_search = list()
        nodes_to_search.append(root)
        nodes_searched = ''
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            nodes_searched += str(node.data) + ' '
        print(nodes_searched)
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

# Day 24: More Linked Lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if not head:
            return None
        current = head
        while current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
        
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 


# Day 25: Running Time and Complexity

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def is_prime(number):
    if number <= 1:
        return False
    sqrt_number = math.sqrt(number)
    if sqrt_number.is_integer():
        return False
    for i in range(2, int(sqrt_number) + 1):
        if number % i == 0:
            return False
    return True

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

number_of_tests = int(input())

for i in range(number_of_tests):
    n = int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')

# Day 26 Nested Logic |

# Enter your code here. Read input from STDIN. Print output to STDOUT

return_day, return_month, return_year = [int(num) for num in input().split(' ')]

due_day, due_month, due_year = [int(num) for num in input().split(' ')]

if return_year < due_year:
    print(0)
elif return_year == due_year:
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        if return_day < due_day:
            print(0)
        else:
            print(15 * (return_day - due_day))
    else:
        print(500 * (return_month - due_month))
        
else:
    print(10000)