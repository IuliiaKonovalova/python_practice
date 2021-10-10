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