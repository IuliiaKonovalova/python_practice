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