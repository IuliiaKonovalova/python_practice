# Python if0else

import math
import os
import random
import re
import sys


# if (n % 2 != 0):
#     print('Weird')
# else:
#     if n in range(6, 21):
#         print('Weird')
#     else:
#         print('Not Weird')


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
# j = int(input())
j = 5
e = 3.0
t = 'here'
# e = float(input())
# t = input()
# Print the sum of both integer variables on a new line.
print(i+j)
# Print the sum of the double variables on a new line.
print(d+e)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+t)



#########################
##                     ##
##  Designer Door Mat  ##
##                     ##
#########################

# N, M = map(int,input().split())
N = 7
M = 21


# Upper part of the mat
for i in range(1, N, 2):
    print((i * ('.|.')).center(M, '-'))

# Middle of the mat
print("welcome".upper().center(M, '-'))

# Lower part of the mat
for i in range(N-2, -1, -2):
    print((i * ('.|.')).center(M, '-'))






# Prints "--HELLO--". 
print("HELLO".center(9, "-"))

