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



height = 7
length = 21

# Upper part of the mat
print('*' * length)
for i in range(1, height, 2):
    print((i * (' ')).center(length, '*'))

# Middle of the mat
print("     ".upper().center(length, '*'))

# Lower part of the mat
for i in range(height-2, -1, -2):
    print((i * (' ')).center(length, '*'))
print('*' * length)



# Prints "--HELLO--". 
print("HELLO".center(9, "-"))

print()



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
##     Nested Lists    ##
##                     ##
#########################



students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Create lists for names and scores data
scores = []
names = []

# Get the date from the list students
for name, score in students:
  scores.append(score)
  names.append(name)

# Delete possible same scores
scores = list(set(scores))

# Sort the list 0-...
scores.sort()

# Get the second lowest score
second_lowest_score = scores[1]

# Create list for second to last students
second_lowest_students = []

#Get the name for the lowest scores
for name, score in students:

  # Check whether there several students with the same scores
  if score == second_lowest_score:

    # Append name to the scores
    second_lowest_students.append(name)

# Sort list according to names
second_lowest_students.sort()

# Get each student with scores
for second_lowest_student in second_lowest_students:
  print(second_lowest_student)


# For hacker Rank

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    #     scores.append(score)
        
    # scores = list(set(scores))
    # scores.sort()
    # lowest_score = scores[1]
    # lowest_students = []
    # for name, score in students:
    #     if score == lowest_score:
    #         lowest_students.append(name)
    
    # lowest_students.sort()
    
    # for student in lowest_students:
    #     print(student)





##############################
##                          ##
##  Finding the percentage  ##
##                          ##
##############################


#  Creating dictionary

    # for _ in range(n):
    #     name, *line = input().split()

    # convert scores string into list
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

student_marks = {}
student_marks['Krishna'] = [67, 68, 69]
student_marks['Arjun'] = [70, 98, 63]
student_marks['Malika'] = [52, 56, 60]
student_marks['Harsh'] = [25, 26.5, 28]
student_marks['Anurag'] = [26, 28, 30]

# Geting keys from the dictionary
values_student_marks = list(student_marks.keys())
# print(values_student_marks)

# Geting values from the dictionary
keys_student_marks = list(student_marks.values())
# print(keys_student_marks)

# Pick a name
student_name_in_student_marks = 'Anurag'

# Get student's scores
student_scores = student_marks['Anurag']

# print(student_scores)
# print(sum(list(student_scores)))

# getting average of the marks, showing 2 places after the decimal.
print("{0:.2f}".format(sum(student_scores)/(len(student_scores))))



##############################
##                          ##
##  collections.Counter()   ##
##                          ##
##############################


# from collections import Counter

# number_of_shoes = int(input())
# shoes = Counter(map(int, input().split()))
# number_of_customer = int(input())

# income = 0

# for i in range(number_of_customer):
#     size, price = map(int, input().split())
#     if shoes[size]: 
#         income += price
#         shoes[size] -= 1

# print(income)


##############################
##                          ##
##   DefaultDict Tutorial   ##
##                          ##
##############################


# from collections import defaultdict
# d = defaultdict(list)


# list1=[]
# n, m = map(int,input().split())
# for i in range(1, n+1):
#     d[input()].append(str(i))


# for i in range(m):
#     b = input()
#     if b in d: print(' '.join(d[b]))
#     else: print(-1)




##################################
##                              ##
##   collections.namedtuple()   ##
##                              ##
##################################

from collections import namedtuple
# import numpy as np
# import pandas as pd

Students = namedtuple('Students','ID MARKS NAME CLASS')
st1 = Students(ID = 1, MARKS = 97, NAME = 'Raynond', CLASS = 7)
st2 = Students(ID = 2, MARKS = 50, NAME = 'Steven', CLASS = 4)
st3 = Students(ID = 3, MARKS = 91, NAME = 'Adrian', CLASS = 9)
st4 = Students(ID = 4, MARKS = 72, NAME = 'Stewart', CLASS = 5)
st5 = Students(ID = 5, MARKS = 80, NAME = 'Peter', CLASS = 6)
st6 = Students(ID = 6, MARKS = 93, NAME = 'Kevin', CLASS = 3)

print(st1)
print(st1.ID)

student_list = []
table_columns = []




# data_length = 3 * 10**5
# fake_data = {
#     "id_code": list(range(data_length)),
#     "letter_code": np.random.choice(list('abcdefgz'), size=data_length),
#     "pine_cones": np.random.randint(low=1, high=100, size=data_length),
#     "area": np.random.randint(low=1, high=100, size=data_length),
#     "temperature": np.random.randint(low=1, high=100, size=data_length),
#     "elevation": np.random.randint(low=1, high=100, size=data_length),}
# dictionary_students = pd.DataFrame(Students)
# print(dictionary_students)


# def iter_with_idx():
#     result_data = []
    
#     idx = {name: i for i, name in enumerate(list(df), start=1)}
    
#     for row in df.itertuples(name=None):
        
#         row_calc = row[idx['pine_cones']] / row[idx['area']]
#         result_data.append(row_calc)
        
#     return result_data

# for student in Students:
#   student_list.append(student)
# print(student_list)

average_marks = 0
n = 3
# for st in range(n+1):
#     average_marks += st.ID[table_columns.index('MARKS')]
# print(average_marks/n)


##################################
##                              ##
##  Collections.OrderedDict()   ##
##                              ##
##################################


# from collections import OrderedDict
# d = OrderedDict()
# print(d)
# for _ in range(int(input())):
#     item, space, quantity = input().rpartition(' ')
#     d[item] = d.get(item, 0) + int(quantity)
# for item, quantity in d.items():
#     print(item, quantity)



##################################
##                              ##
##           Word Order         ##
##                              ##
##################################


from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
  """
  Counter that remembers the order elements are first seen
  """
  def __repr__(self):
    return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))
  def __reduce__(self):
    return self.__class__, (OrderedDict(self),)


oc = OrderedCounter('adddddbracadabra')

print(oc)

OrderedCounter(OrderedDict([('a', 5), ('d', 6), ('b', 2), ('r', 2), ('c', 1)]))

# from collections import Counter, OrderedDict

# class OrderedCounter(Counter, OrderedDict):
#     pass

# words_dictionary = OrderedCounter(input() for _ in range(int(input())))
# print(len(words_dictionary))
# print(*words_dictionary.values())



##################################
##                              ##
##      Collections.deque()     ##
##                              ##
##################################

# from collections import deque

# dueque_to_work_with = deque()
# for _ in range(int(input())):
#     input_to_work_on, *args = input().split()
#     getattr(dueque_to_work_with, input_to_work_on)(*args)
# [print(x, end=' ') for x in d]


# dueque_to_work_with = deque()

# for _ in range(int(input())):
#     input_to_work_on = input().split()
#     getattr(dueque_to_work_with, input_to_work_on[0])(*[input_to_work_on[1]] if len(input_to_work_on) > 1 else [])
    
# print(*[item for item in dueque_to_work_with])


##################################
##                              ##
##             Lists            ##
##                              ##
##################################

# if __name__ == '__main__':
#     N = int(input())
#     tasks_list = []
#     solution_list = []
    
#     for i in range(N):
#         tasks = input().split()
#         tasks_list.append(tasks)
        
#     for i in range(len(tasks_list)):
#         if tasks_list[i][0] == 'print':
#             print(solution_list)
#         elif tasks_list[i][0] == 'insert':
#             index_in_task = int(tasks_list[i][1])
#             number_in_task = int(tasks_list[i][2])
#             solution_list.insert(index_in_task, number_in_task)
#         elif tasks_list[i][0] == 'remove':
#             solution_list.remove(int(tasks_list[i][1]))
#         elif tasks_list[i][0] == 'append':
#             solution_list.append(int(tasks_list[i][1]))
#         elif tasks_list[i][0] == 'sort':
#                solution_list.sort()
#         elif tasks_list[i][0] == 'pop':
#             if len(tasks_list[i]) > 1:
#                solution_list.pop(int(tasks_list[i][1])) 
#             solution_list.pop()
#         elif tasks_list[i][0] == 'reverse':
#             solution_list.reverse()     
            
# n = input()
# l = []
# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#       eval('arr.{0}{1}'.format(cmd,tuple(map(int,args))))
#     else:
#       print(l)

##################################
##                              ##
##            Tuples            ##
##                              ##
##################################

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     print(hash(integer_list))

##################################
##                              ##
##   itertools.permutations()   ##
##                              ##
##################################


# from itertools import permutations

# word, number = input().split()
# print(*[''.join(i) for i in permutations(sorted(word), int(number))], sep = '\n')



##################################
##                              ##
##   itertools.combinations()   ##
##                              ##
##################################

# from itertools import combinations

# word, number = input().split()

# for i in range(1, int(number) + 1):
#     for j in combinations(sorted(word), i):
#         print(''.join(j))





###################################################
##                                               ##
##   itertools.combinations_with_replacement()   ##
##                                               ##
###################################################


# from itertools import combinations_with_replacement

# word, number = input().split()

# print(*[''.join(i) for i in combinations_with_replacement(sorted(word), int(number))], sep = '\n')


###################################################
##                                               ##
##                 Linear algebra                ##
##                                               ##
###################################################

# import numpy

# number = int(input())

# list_of_num = numpy.array([input().split() for _ in range(number)], float)
# numpy.set_printoptions(legacy = '1.13')
# print(numpy.linalg.det(list_of_num))



###################################################
##                                               ##
##                 Inputs                        ##
##                                               ##
###################################################

# numbers = input().split()
# x = int(numbers[0])

# if x**3 + x**2 + x + 1 == int(numbers[1]):
#     print(True)



# numbers = input().split()
# x = int(numbers[0])

# print(eval(input()) == int(numbers[1]))

###################################################
##                                               ##
##                 Eval()                        ##
##                                               ##
###################################################
# input() = print(2 +3)
# input_to_eval = input()

# eval(input_to_eval)

###################################################
##                                               ##
##                 Athlete Sort                  ##
##                                               ##
###################################################


# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n, m = list(map(int, input().split()))

    
#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().split())))

#     k = int(input())
    
#     # sorting for the index 
#     arr.sort(key=lambda x: x[k])
    

#     for el in arr:
#           # unpacking
#         print(*el)



###################################################
##                                               ##
##                 Any or all                    ##
##                                               ##
###################################################

# amount_of_numbers = input()

# numbers = list(map(int, input().split()))

# print(all([any([str(element) == str(element)[::-1] for element in numbers]), any([int(element) > 0 for element in numbers])]))

###################################################
##                                               ##
##                 Find method                   ##
##                                               ##
###################################################

word = "bananana"
i = word.find("ana")
print(i)


###################################################
##                                               ##
##                  ginortS                      ##
##                                               ##
###################################################


x = sorted('Sorting1234')
print(x)

initial_input = 'Sorting1234'
initial_input = sorted(initial_input)

upper = ''
lower = ''
even = ''
odds = ''

for i in initial_input:
  if i.islower():
    lower += i
  elif i.isupper():
    upper += i
  elif int(i) % 2 == 0:
    even += i
  elif int(i) % 2 != 0:
    odds += i
print(lower + upper + odds + even) 




###################################################
##                                               ##
##                  sWAP cASE                    ##
##                                               ##
###################################################

def swap_case(s):
  new_string = ''
  for character in s:
    if character.isupper():
      character = character.lower()
    else:
      character = character.upper()
    new_string += ''.join(character)
  return new_string

s = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(s)
print(result)


###################################################
##                                               ##
##            String Split and Join              ##
##                                               ##
###################################################

def split_and_join(line):
  return '-'.join(line.split(' '))

line1 = 'this is a string'
result = split_and_join(line1)
print(result)


###################################################
##                                               ##
##            What's Your Name?                  ##
##                                               ##
###################################################


def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')


###################################################
##                                               ##
##                     Mutations                 ##
##                                               ##
###################################################

def mutate_string(string, position, character):
  string_to_list = list(string)
  string_to_list[position] = character
  return ''.join(string_to_list)

###################################################
##                                               ##
##                Find a string                  ##
##                                               ##
###################################################


def count_substring(string, sub_string):
  count_sub_strings = 0
  length_of_sub_string = len(sub_string)
  for i in range(len(string)):
    new_strings = string[i:i + length_of_sub_string]
    if new_strings == sub_string:
      count_sub_strings += 1
  return count_sub_strings




###################################################
##                                               ##
##                string validators              ##
##                                               ##
###################################################


# if __name__ == '__main__':
#     s = input()
    
#     print(any(i.isalnum() for i in s))
#     print(any(i.isalpha() for i in s))
#     print(any(i.isdigit() for i in s))
#     print(any(i.islower() for i in s))
#     print(any(i.isupper() for i in s))


###################################################
##                                               ##
##                text alignment                 ##
##                                               ##
###################################################


# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



###################################################
##                                               ##
##                Merge the tools!               ##
##                                               ##
###################################################
string1 = 'AABCAAADA'
k1 = 3
def merge_the_tools(string, k):
  new_string = ''

  for i in range(0, len(string), k):
    for letter in string[i:i+k]:
      if letter not in new_string:
        new_string = new_string + letter
    print(new_string)
    new_string = ''

string1 = 'AABCAAADA'
k1 = 3

result_of_merging = merge_the_tools(string1, k1)

###################################################
##                                               ##
##            Introduction to Sets               ##
##                                               ##
###################################################

def average(array):
    # your code goes here
    
    array_to_set = set(array)
    return sum(array_to_set)/len(array_to_set)


###################################################
##                                               ##
##            Symmetric Difference               ##
##                                               ##
###################################################


# a, b = [set(input().split()) for _ in range(4)][1::2]

# a_difference = a.difference(b)
# b_difference = b.difference(a)

# a_b_union_difference = a_difference.union(b_difference)
# print('\n'.join(sorted(list(a_b_union_difference), key = int)))


###################################################
##                                               ##
##                   Set.add()                   ##
##                                               ##
###################################################



# a = set()
# [a.add(input()) for _ in range(int(input()))]
# print(len(a))





###################################################
##                                               ##
##       Set .discard(), .remove() & .pop()      ##
##                                               ##
###################################################


# num = int(input())
# data = set(map(int, input().split()))
# operations = int(input())

# for x in range(operations):
#   operation = input().split()
#   if operation[0] == "remove":
#     data.remove(int(operation[1]))
#   elif operation[0] == "discard":
#     data.discard(int(operation[1]))
#   else:
#     data.pop()
    
# print(sum(data))


###################################################
##                                               ##
##                   Set.union()                 ##
##                                               ##
###################################################


# number1 = int(input())
# english_newspaper = list(input().split())
# number2 = int(input())
# french_newspaper = list(input().split())

# print(len(set(english_newspaper).union(set(french_newspaper))))


###################################################
##                                               ##
##          Set .intersection() Operation        ##
##                                               ##
###################################################


# number1 = int(input())
# english_newspaper = list(input().split())
# number2 = int(input())
# french_newspaper = list(input().split())

# print(len(set(english_newspaper).intersection(set(french_newspaper))))


###################################################
##                                               ##
##          Set .difference () Operation         ##
##                                               ##
###################################################


# number1 = int(input())
# english_newspaper = list(input().split())
# number2 = int(input())
# french_newspaper = list(input().split())

# print(len(set(english_newspaper).difference(set(french_newspaper))))

###################################################
##                                               ##
##   Set .symmetric_difference () Operation      ##
##                                               ##
###################################################


# number1 = int(input())
# english_newspaper = list(input().split())
# number2 = int(input())
# french_newspaper = list(input().split())

# print(len(set(english_newspaper).symmetric_difference(set(french_newspaper))))




###################################################
##                                               ##
##                   Set Mutation                ##
##                                               ##
###################################################



# if __name__ == '__main__':
#     (_, A) = (int(input()),set(map(int, input().split())))
#     B = int(input())
#     for _ in range(B):
#         (command, newSet) = (input().split()[0],set(map(int, input().split())))
#         getattr(A, command)(newSet)

#     print (sum(A))


###################################################
##                                               ##
##               The Captian's Room              ##
##                                               ##
###################################################



# k,arr = int(input()),list(map(int, input().split()))

# my_set = set(arr)

# print(((sum(my_set)*k)-(sum(arr)))//(k-1))



###################################################
##                                               ##
##                   Check Subset                ##
##                                               ##
###################################################



# for _ in range(int(input())):
#     x, a, z, b = input(), set(input().split()), input(), set(input().split())
#     print(a.issubset(b))



###################################################
##                                               ##
##               Check Strict Superset           ##
##                                               ##
###################################################


# def is_strict_superset(a,b):
    
#     return b.issubset(a) and not(a.issubset(b))

# a = set(int(x) for x in input().split(' '))
# n = int(input())
# result = True

# for _ in range(n):
#     b = set(int(x) for x in input().split(' '))
#     result &= is_strict_superset(a,b)
    
# print(result)


###################################################
##                                               ##
##               Shape and reshape               ##
##                                               ##
###################################################

# import numpy

# print(numpy.array(input().split(),int).reshape(3,3))




###################################################
##                                               ##
##                    Arrays                     ##
##                                               ##
###################################################





# def arrays(arr):
#     # complete this function
#     # use numpy.array
#     return numpy.array(arr[::-1], float)




###################################################
##                                               ##
##              Transpose and Flatten            ##
##                                               ##
###################################################


# import numpy



# n, m = map(int, input().split())
# array = numpy.array([input().split() for _ in range(n)], int)

# print (array.transpose())
# print (array.flatten())



###################################################
##                                               ##
##                    concatenate                ##
##                                               ##
###################################################



# import numpy

# n, m, p = map(int, input().split())
# my_numpy_array1 = numpy.array([input().split() for _ in range(n)], int)
# my_numpy_array2 = numpy.array([input().split() for _ in range(m)], int)

# print(numpy.concatenate((my_numpy_array1, my_numpy_array2), axis = 0))

###################################################
##                                               ##
##                 zeros and ones                ##
##                                               ##
###################################################

# import numpy 

# numbers = tuple(map(int, input().split()))

# print(numpy.zeros(numbers, dtype = numpy.int))

# print(numpy.ones(numbers, dtype = numpy.int))


###################################################
##                                               ##
##          Birthday Cake Candles                ##
##                                               ##
###################################################



# def birthdayCakeCandles(candles):
#     return candles.count(max(candles))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     candles_count = int(input().strip())

#     candles = list(map(int, input().rstrip().split()))

#     result = birthdayCakeCandles(candles)

#     fptr.write(str(result) + '\n')

#     fptr.close()

###################################################
##                                               ##
##                 Eye and Identity              ##
##                                               ##
###################################################

# print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


###################################################
##                                               ##
##                 Array Mathematics             ##
##                                               ##
###################################################


# import numpy

# n, m = map(int, input().split())

# first_array, second_array = (numpy.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))



# # print(first_array)
# # print(second_array)

# print(numpy.add(first_array, second_array))
# print(numpy.subtract(first_array, second_array))
# print(numpy.multiply(first_array, second_array))
# print(numpy.floor_divide(first_array, second_array))
# print(numpy.mod(first_array, second_array))
# print(numpy.power(first_array, second_array))



###################################################
##                                               ##
##             floor, ceil, rint                 ##
##                                               ##
###################################################


# import numpy

# numpy.set_printoptions(sign=' ')

# a = numpy.array(input().split(),float)

# print(numpy.floor(a))
# print(numpy.ceil(a))
# print(numpy.rint(a))


###################################################
##                                               ##
##                  sum and prod                 ##
##                                               ##
###################################################



# import numpy

# n, m = map(int, input().split())
# A = numpy.array([input().split() for _ in range(n)],int)
# print(numpy.prod(numpy.sum(A, axis=0), axis=0))


###################################################
##                                               ##
##                  min and max                  ##
##                                               ##
###################################################


# n, m = map(int,input().split())

# list_to_change = [list(map(int,input().split())) for i in range(n)]

# array_to_work_on = numpy.array(list_to_change)

# print(max(numpy.min(array_to_work_on, axis = 1)))




###################################################
##                                               ##
##              Mean, Var, and St                ##
##                                               ##
###################################################



# import numpy
# array = []
# n, m = map(int, input().split())
# for _ in range(n): array.append(list(map(int, input().split())))
# array = numpy.array(array)
# print(numpy.mean(array, axis=1))
# print(numpy.var(array, axis=0))
# print(round(numpy.std(array), 11))



###################################################
##                                               ##
##                Dot and cross                  ##
##                                               ##
###################################################


# number = int(input())

# first_array = numpy.array([input().split() for _ in range(number)], int)
# second_array = numpy.array([input().split() for _ in range(number)], int)

# # print(first_array)
# # print(second_array)
# print(numpy.dot(first_array, second_array))


###################################################
##                                               ##
##              Inner and outer                  ##
##                                               ##
###################################################


# first_array = numpy.array(input().split(), int)
# second_array = numpy.array(input().split(), int)

# print(numpy.inner(first_array, second_array))
# print(numpy.outer(first_array, second_array))


###################################################
##                                               ##
##                Polynomials                    ##
##                                               ##
###################################################


# n = list(map(float,input().split()));
# m = input();
# print(numpy.polyval(n,int(m)));


###################################################
##                                               ##
##             Default Arguments                 ##
##                                               ##
###################################################


# class EvenStream(object):
#     def __init__(self):
#         self.current = 0

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# class OddStream(object):
#     def __init__(self):
#         self.current = 1

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# def print_from_stream(n, stream=None):
#     if stream is None:
#         stream = EvenStream()
#     for _ in range(n):
#         print(stream.get_next())


# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())


###################################################
##                                               ##
##             Intertools.product()              ##
##                                               ##
###################################################

# from itertools import product

# first_tuple = list(map(int, input().split()))
# second_tuple = list(map(int, input().split()))




# print(*product(first_tuple, second_tuple))