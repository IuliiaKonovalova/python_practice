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



#########################
##                     ##
##  String Formatting  ##
##                     ##
#########################




def print_formatted(number):

  # Empty list which takes lists of numbers
  list_of_numbers = []

  # Iteration through the number to create oct, hex, and bin numbers
  for num in range(1, number+1):
    decimal_number = str(num)
    oct_number = str(oct(num))[2:]
    hex_number = str(hex(num))[2:].upper()
    bin_number = str(bin(num))[2:]

    # Add list for each combination
    list_of_numbers.append([decimal_number, oct_number, hex_number, bin_number])

  # Count length of the biggest binary number
  column_width = len(list_of_numbers[-1][-1]) 

  # Loop through each list in list_of numbers
  for each_line in list_of_numbers:

    # Loop through each number of the each list and add additional space to the right for each number
    print(*(each_number.rjust(column_width, '-') for each_number in each_line))

print_formatted(10)



#########################
##                     ##
##  Alphabet Rangoli   ##
##                     ##
#########################

import string
alphabet_letters = string.ascii_lowercase


n = 5

# Create a list for lines
list_of_lines = []

# Iterate through the alphabet string
for i in range(n):

  # Join letters for each half of a line
  string_of_letters = "-".join(alphabet_letters[i:n])

  # Append each line:
  # 1. reverse line
  # 2. initial line without the first index (middle letter)
  # 3. center elements according to the size
  list_of_lines.append((string_of_letters[::-1]+string_of_letters[1:]).center(4*n-3, "-"))

# Print reverse list and list with each line joining by \n
print('\n'.join(list_of_lines[:0:-1]+list_of_lines))


#########################
##                     ##
##     Capitalize!     ##
##                     ##
#########################

def solve(s):
    list_of_words = s.split()
    # If we need to preserve spaces between words:
    # list_of_words = s.split(' ')
    return ' '.join((word.capitalize() for word in list_of_words))

print(solve('hello   123world'))


#########################
##                     ##
##   The Minion Game   ##
##                     ##
#########################


    # your code goes here
def minion_game(string_word):

  # exclude vowels
  vowels = ['A', 'E', 'I', 'O', 'U']

  # Integers to control scores 
  stuart = 0
  kevin = 0

  # Iterate through the string
  for i in range(len(string_word)):

    print(string_word[i])
    
    if string_word[i] in vowels:
      kevin += len(string_word) - i
      print(f'kevin {len(string_word) - i}')

    else:
      stuart += len(string_word) - i
      print(f'stuart {len(string_word) - i}')


  # Winning points
  if stuart > kevin:
    print("Stuart" + ' ' + '%d' % stuart)
  elif kevin > stuart:
    print("Kevin" + ' ' + '%d' % kevin)
  else:
    print("Draw")


minion_game('BANANA')



###########################
##                       ##
##  List Comprehensions  ##
##                       ##
###########################


x = 1
y = 2
z = 2
n = 3
    
print ([[i, j, k] for i  in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n ])




#################################
##                             ##
##  Find the Runner-Up Score!  ##
##                             ##
#################################



#  HackerRank i had to put list_runners = arr
list_runners = [2, 3, 6, 6, 5]

# print(max(list_runners))


def runner_up_find(list_runner):

  # define runner_up variable to compare
  runner_up = 0

  # Iterate through the list to find the runner-up
  for i in list_runner:

    # Exclude the winners
    if i == max(list_runner):
      pass

    else:
      # Find the runner-up
      if runner_up < i:
        runner_up = i
  return print(runner_up)
runner_up_find(list_runners)

def runner_up_find2(list_runner):
  
    winner = max(list_runner)

    while winner == max(list_runner):
        list_runner.remove(max(list_runner))

    print(max(list_runner))


runner_up_find2(list_runners)

#########################
##                     ##
##   Merge the Tools   ##
##                     ##
#########################


